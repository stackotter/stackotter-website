import { GetStaticProps } from "next"
import React, { FunctionComponent } from "react"
import { ArticleMetadata, getArticleIds, getArticleMetadata } from "../../lib/articles"
import "github-markdown-css"
import Link from "next/link"
import Page from "../../components/page"

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
    <Page>
      <h1>Blog</h1>
      <p>I mostly write about my personal projects and sometimes I'll create writeups for ctf challenges. At the moment most of the articles are going to be about my journey in creating <a href="https://github.com/stackotter/delta-client">delta client</a> as that is what I'm currently spending most of my time on.</p>
      <p>I'll bring you along on my adventure's in open source software development, reverse engineering Minecraft Java Edition, optimising code (yeah it's nerdy), and many other things computers.</p>
      <h2>Articles</h2>
      { listItems.length == 0 ?
        <p>No articles yet!</p> :
        <ul>{listItems}</ul> }
    </Page>
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