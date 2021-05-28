import { GetStaticProps } from 'next'
import { getArticleHTML } from '../lib/articles'
import { FunctionComponent } from 'react'
import MarkdownPage from '../components/markdown-page'
import Head from 'next/head'

type ContactProps = {
  html: string
}

const ContactPage: FunctionComponent<ContactProps> = (contact) => {
  return (
    <div>
      <Head>
        <title>stackotter - contact</title>
      </Head>
      <MarkdownPage html={contact.html}/>
    </div>
  )
}

export default ContactPage

export const getStaticProps: GetStaticProps<ContactProps> = async () => {
  const html = await getArticleHTML("_contact")

  return {
    props: {
      html,
    }
  }
}