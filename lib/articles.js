import fs from 'fs'

const apiUrl = "https://api.github.com/markdown"
const markdownDir = "articles/"

export function getArticlesFileNames() {
  var paths = []
  let files = fs.readdirSync(markdownDir)
  for (var i = 0; i < files.length; i++) {
    let file = files[i]
    if (file.endsWith(".md")) {
      paths.push(file)
    }
  }
  return paths
}

export function getArticlePaths() {
  let files = getArticlesFileNames()

  var paths = []
  for (var i = 0; i < files.length; i++) {
    let file = files[i]
    let path = file.slice(0, -3)
    paths.push({
      params: {
        id: path
      }
    })
  }

  return paths
}

export async function getArticlesHTML() {
  let articles = {}

  let files = getArticlesFileNames()
  for (var i = 0; i < files.length; i++) {
    let fileName = files[i]
    let markdown = fs.readFileSync(markdownDir + fileName).toString()
    let html = await markdownToHTML(markdown)
    articles[fileName.slice(0, -3)] = {
      content: html
    }
  }

  return articles
}

// convert `markdown` to html using GitHub's markdown API
async function markdownToHTML(markdown) {
  let html = await fetch(apiUrl, {
    body: JSON.stringify({
      text: markdown,
      mode: "gfm"
    }),
    headers: {
      Accept: "application/vnd.github.v3+json"
    },
    method: "POST"
  }).then((res) => {
    return res.text()
  })
  return html
}
