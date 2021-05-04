import { useRouter } from 'next/router'
import { getArticlePaths, getArticlesHTML } from '../../lib/articles'

import Page from '../../components/page'
import markdownStyles from 'github-markdown-css'

export default function Article({ articles }) {
  const router = useRouter()
  const { id } = router.query

  let article = articles[id]

  return (
    <Page>
      <div className="markdown-body" dangerouslySetInnerHTML={{ __html: article.content }}/>
    </Page>
  )
}

export async function getStaticProps() {
  const articles = await getArticlesHTML()
  return {
    props: {
      articles,
    }
  }
}

export async function getStaticPaths() {
  const paths = getArticlePaths()
  console.log(paths)
  return {
    paths,
    fallback: false
  }
}