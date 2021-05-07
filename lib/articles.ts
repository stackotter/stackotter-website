import yaml from 'yaml'
import fs from 'fs'

const apiUrl = 'https://api.github.com/markdown'
const markdownDir = 'articles/'
const articleMetaFile = 'articles/articles.yaml'

export type Article = {
  html: string
  metadata?: ArticleMetadata
}

export type ArticleMetadata = {
  title: string
  date: string
  updated?: string
}

// get array of all articles (articles starting with _ are ignored)
export function getArticleIds(): Array<string> {
  var ids: Array<string> = []
  let files = fs.readdirSync(markdownDir)
  for (var i = 0; i < files.length; i++) {
    let file = files[i]
    if (file.endsWith('.md') && !file.startsWith("_")) {
      let id = file.slice(0, -3)
      ids.push(id)
    }
  }
  return ids
}

// get article with id `id`
export async function getArticle(id): Promise<Article> {
  let metadata = getArticleMetadata(id)
  let html = await getArticleHTML(id)

  return {
    html: html,
    metadata: metadata
  }
}

// parse `markdownDir`/articles.yaml
export function getConfig(): { [key: string]: any } {
  let fileContents = fs.readFileSync(articleMetaFile).toString()
  let parsed = yaml.parse(fileContents)
  return parsed as { [key: string]: any }
}

// get metadata for article (title, data written and last update)
export function getArticleMetadata(id): ArticleMetadata | undefined {
  let config = getConfig()
  let articles = config["articles"] as { [key: string]: ArticleMetadata }
  return articles[id]
}

// get html for article in `markdownDir`/`id`.md
export async function getArticleHTML(id): Promise<string> {
  let markdown = fs.readFileSync(markdownDir + id + '.md').toString()
  let html = await markdownToHTML(markdown)
  return html
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
