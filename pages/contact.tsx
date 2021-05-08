import { GetStaticProps } from 'next'
import { getArticleHTML } from '../lib/articles'
import { FunctionComponent } from 'react'
import MarkdownPage from '../components/markdown-page'

type ContactProps = {
  html: string
}

const ContactPage: FunctionComponent<ContactProps> = (contact) => {
  return <MarkdownPage html={contact.html}/>
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