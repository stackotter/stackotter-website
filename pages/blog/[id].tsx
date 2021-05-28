import { GetStaticPaths, GetStaticProps } from 'next'
import { Article, getArticle, getArticleIds } from '../../lib/articles'
import { FunctionComponent } from 'react'
import { ParsedUrlQuery } from 'querystring'
import MarkdownPage from '../../components/markdown-page'
import Head from 'next/head'

interface Params extends ParsedUrlQuery {
  id: string
}

const ArticlePage: FunctionComponent<Article> = (article) => {
  return (
    <div>
      <Head>
        <title>{article.metadata.title}</title>
      </Head>
      <MarkdownPage html={article.html}/>
    </div>
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