const { configureSitemap } = require('@sergeymyssak/nextjs-sitemap');
const fs = require("fs")

const markdownDir = "articles/"

function getArticlesFileNames() {
  var paths = []
  let files = fs.readdirSync(markdownDir)
  for (var i = 0; i < files.length; i++) {
    let file = files[i]
    if (file.endsWith(".md") && !file.startsWith("_")) {
      paths.push(file)
    }
  }
  return paths
}

function getDynamicPaths() {
  const data = getArticlesFileNames()
  return data.map((item) => `/blog/${item.slice(0, -3)}`)
}

let paths = getDynamicPaths()
const Sitemap = configureSitemap({
  baseUrl: 'https://stackotter.dev',
  include: paths,
  exclude: ['/blog/[id]'], // or exclude: ['/project/*']
  excludeIndex: true,
  pagesConfig: {
    '/blog/*': {
      priority: '1.0',
      changefreq: 'weekly',
    },
  },
  isTrailingSlashRequired: true,
  targetDirectory: __dirname + '/public',
  pagesDirectory: __dirname + '/pages',
})
Sitemap.generateSitemap()