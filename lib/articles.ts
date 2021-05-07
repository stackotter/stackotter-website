import fs from 'fs'

const apiUrl = 'https://api.github.com/markdown'
const markdownDir = 'articles/'

export type Article = {
  html: string
}

export function getArticlesFileNames(): Array<string> {
  var paths: Array<string> = []
  let files = fs.readdirSync(markdownDir)
  for (var i = 0; i < files.length; i++) {
    let file = files[i]
    if (file.endsWith('.md') && !file.startsWith("_")) {
      paths.push(file)
    }
  }
  return paths
}

export function getArticleIds(): Array<string> {
  let files = getArticlesFileNames()

  var paths: Array<string> = []
  for (var i = 0; i < files.length; i++) {
    let file = files[i]
    let id = file.slice(0, -3)
    paths.push(id)
  }

  return paths
}

export async function getArticle(path): Promise<Article> {
  let markdown = fs.readFileSync(markdownDir + path + '.md').toString()
  let html = await markdownToHTML(markdown)
  let article = {
    html: html
  }

  return article
}

// convert `markdown` to html using GitHub's markdown API
async function markdownToHTML(markdown): Promise<string> {
  let html = await fetch(apiUrl, {
    body: JSON.stringify({
      text: markdown,
      mode: 'gfm'
    }),
    headers: {
      Accept: 'application/vnd.github.v3+json'
    },
    method: 'POST'
  }).then((res) => {
    return res.text()
  })
  return html
}
