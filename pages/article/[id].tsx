import 'github-markdown-css'
import { GetStaticPaths, GetStaticProps } from 'next'
import { Article, getArticle, getArticleIds } from '../../lib/articles'
import { FunctionComponent } from 'react'
import { ParsedUrlQuery } from 'querystring'
import Page from '../../components/page'
import styles from '../../styles/page.module.css'
import MarkdownPage from '../../components/markdown-page'

interface Params extends ParsedUrlQuery {
  id: string
}

const ArticlePage: FunctionComponent<Article> = (article) => {
  return (
    <MarkdownPage html={article.html}/>
  )
}

export default ArticlePage

export const getStaticProps: GetStaticProps<Article, Params> = async (context) => {
  const id = context.params!.id
  const article = await getArticle(id)

  return {
    props: article,
  }
}

export const getStaticPaths: GetStaticPaths = async () => {
  const ids = getArticleIds()
  const paths = ids.map((id) => {
    return {
      params: { id }, 
    }
  })

  return {
    paths,
    fallback: false
  }
}