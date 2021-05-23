import { GetStaticProps } from 'next'
import { getArticleHTML } from '../lib/articles'
import { FunctionComponent } from 'react'
import MarkdownPage from '../components/markdown-page'

type AboutProps = {
  html: string
}

const AboutPage: FunctionComponent<AboutProps> = (about) => {
  return <MarkdownPage html={about.html}/>
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