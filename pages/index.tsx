import { GetStaticProps } from 'next'
import { getArticleHTML } from '../lib/articles'
import { FunctionComponent } from 'react'
import MarkdownPage from '../components/markdown-page'
import Head from 'next/head'

type AboutProps = {
  html: string
}

const AboutPage: FunctionComponent<AboutProps> = (about) => {
  return (
    <div>
      <Head>
        <title>stackotter</title>
      </Head>
      <MarkdownPage html={about.html}/>
    </div>
  )
}

export default AboutPage

export const getStaticProps: GetStaticProps<AboutProps> = async () => {
  const html = await getArticleHTML("_about")

  return {
    props: {
      html,
    }
  }
}