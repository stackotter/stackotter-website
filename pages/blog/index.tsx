import { GetStaticProps } from "next"
import React, { FunctionComponent } from "react"
import { ArticleMetadata, getArticleIds, getArticleMetadata } from "../../lib/articles"
import "github-markdown-css"
import Link from "next/link"
import Page from "../../components/page"
import Head from "next/head"

type BlogProps = {
  articles: { [id: string]: ArticleMetadata }
}

const BlogHome: FunctionComponent<BlogProps> = function({ articles }) {
  let listItems = []
  for (let id in articles) {
    let article = articles[id]
    let listItem = (
      <li key={id}>
        <Link href={`/blog/${id}`}>{article.title}</Link> {/* link to article */}
        <span> — </span> {/* divider */}
        <em>{article.date}</em> {/* date written */}
      </li>
    )
    listItems.push(listItem)
  }

  return (
    <div>
      <Head>
        <title>stackotter - blog</title>
        <meta name="description" content="Join me on my adventures in Swift, optimisation, functional programming and cybersecurity. I don't write articles often, but hopefully when I do you'll find it interesting." />
      </Head>
      <Page>
        <h1>Blog</h1>
        <p>Join me on my adventures in Swift, optimisation, functional programming and cybersecurity. I don't write articles often, but hopefully when I do you'll find it interesting.</p>
        <h2>Articles</h2>
        { listItems.length == 0 ?
          <p>No articles yet!</p> :
          <ul>{listItems}</ul> }
      </Page>
    </div>
  )
}

export default BlogHome

export const getStaticProps: GetStaticProps<BlogProps> = async () => {
  let articlesIds = getArticleIds()
  let articles: { [id: string]: ArticleMetadata } = {}
  articlesIds.forEach((id) => {
    articles[id] = getArticleMetadata(id)
  })
  return {
    props: {
      articles
    }
  }
}