import { GetStaticProps } from "next"
import { FunctionComponent } from "react"
import MarkdownPage from "../../components/markdown-page"
import Page from "../../components/page"
import { ArticleMetadata, getArticleIds, getArticleMetadata } from "../../lib/articles"
import "github-markdown-css"

type BlogProps = {
  articles: { [id: string]: ArticleMetadata }
}

const BlogHome: FunctionComponent<BlogProps> = function({ articles }) {
  return (
    <Page>
      <h1>Hello World</h1>
      <p>hello</p>
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