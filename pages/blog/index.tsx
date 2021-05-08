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
      <li>
        <Link href={`/blog/${id}`}>{article.title}</Link> {/* link to article */}
        <span> — </span> {/* divider */}
        <em>{article.date}</em> {/* date written */}
      </li>
    )
    listItems.push(listItem)
  }

  return (
    <Page>
      <h2>Blog</h2>
      <p>I mostly write about my personal projects and sometimes I'll create writeups for ctf challenges. At the moment most of the articles are going to be about my journey in creating <a href="https://github.com/stackotter/delta-client">delta client</a> as that is what I'm currently spending most of my time on.</p>
      <p>I'll bring along on my adventure's in open source software development, reverse engineering Minecraft Java Edition, optimising code (one of my favourite things to do at the moment (yeah it's nerdy, I know (that's a lot of brackets))).</p>
      <h2>Articles</h2>
      <ul>{listItems}</ul>
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