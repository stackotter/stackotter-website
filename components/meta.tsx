import { FunctionComponent } from "react"
import Head from 'next/head'

const Meta: FunctionComponent = () => {
  return (
    <Head>
      <title>stackotter.dev</title>
      <link rel="manifest" href="/site.webmanifest" />
      <link rel="apple-touch-icon" sizes="180x180" href="/favicon/apple-touch-icon.png" />
      <link rel="icon" type="image/png" sizes="32x32" href="/favicon/favicon-32x32.png" />
      <link rel="icon" type="image/png" sizes="16x16" href="/favicon/favicon-16x16.png" />
    </Head>
  )
}

export default Meta