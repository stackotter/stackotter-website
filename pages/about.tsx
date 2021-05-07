import 'github-markdown-css'
import { GetStaticPaths, GetStaticProps } from 'next'
import { Article, getArticle, getArticleIds } from '../lib/articles'
import { FunctionComponent } from 'react'
import { ParsedUrlQuery } from 'querystring'
import Page from '../components/page'
import styles from '../../styles/page.module.css'
import MarkdownPage from '../components/markdown-page'

interface Params extends ParsedUrlQuery {
  id: string
}

const AboutPage: FunctionComponent<Article> = (article) => {
  return (
    // <Page>
    //   <div className={ "markdown-body " + styles.markdown } dangerouslySetInnerHTML={{ __html: article.html }}/>
    // </Page>
    <MarkdownPage html={article.html}/>
  )
}

export default AboutPage

export const getStaticProps: GetStaticProps<Article, Params> = async (context) => {
  const article = await getArticle("_about")

  return {
    props: article,
  }
}