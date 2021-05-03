import Head from 'next/head'
import styles from '../styles/Home.module.css'

export default function Home() {
  return (
    <div className={styles.container}>
      <Head>
        <title>stackotter</title>
        <meta name="description" content="stackotter's personal website" />
      </Head>

      <main className={styles.main}>
        hello
      </main>
    </div>
  )
}
