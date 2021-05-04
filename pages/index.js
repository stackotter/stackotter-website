import Head from 'next/head'
import ReactMarkdown from 'react-markdown'
import gfm from 'remark-gfm'
import styles from '../styles/Home.module.css'
import markdownStyles from 'github-markdown-css'
import { useEffect, useState } from 'react'

const markdown = `# Gutentag

Hi I'm stackotter.

\`\`\`swift
let name = "stackotter"
let greeting = "hello, from \(name)"
print(greeting)
\`\`\`
`

export default function Home() {
  const [appState, setAppState] = useState({
    loading: false,
    content: null,
  })

  useEffect(() => {
    setAppState({ loading: true })
    const apiUrl = "https://api.github.com/markdown"
    fetch(apiUrl, {
      body: JSON.stringify({
        text: markdown,
        mode: "gfm"
      }),
      headers: {
        Accept: "application/vnd.github.v3+json"
      },
      method: "POST"
    })
    .then((res) => {
      return res.text()
    })
    .then((res) => {
      console.log(res)
      setAppState({ content: res, loading: false })
    })
  }, [setAppState])

  var article
  if (appState.loading) {
    article = <div>Loading..</div>
  } else {
    article = <div className="markdown-body" dangerouslySetInnerHTML={{ __html: appState.content }}/>
  }
  return (
    <div className={styles.container}>
      <Head>
        <title>stackotter</title>
        <meta name="description" content="stackotter's personal website" />
        <link rel="stylesheet" href="github-markdown.css"/>
      </Head>

      <main className={styles.main}>
        {article}
      </main>
    </div>
  )
}
