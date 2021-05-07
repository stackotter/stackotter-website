import { GetStaticProps } from "next"
import { FunctionComponent } from "react"
import MarkdownPage from "../../components/markdown-page"
import { ArticleMetadata, getArticleIds, getArticleMetadata } from "../../lib/articles"

type BlogProps = {
  articles: { [id: string]: ArticleMetadata }
}

const BlogHome: FunctionComponent<BlogProps> = function({ articles }) {
  return <MarkdownPage html="hi"/>
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