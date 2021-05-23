import styles from '../styles/header.module.css'
import Link from 'next/link'
import { FunctionComponent } from 'react'

const Header: FunctionComponent = () => {
  return (
    <header className={styles.header}>
      <a href="/">
        <img src="/image/otter.png" className={styles.logo}/>
      </a>

      <h1 className={[styles.h1].join(" ")}>stackotter.dev</h1>

      <div id={styles.nav}>
        <Link href="/about" >
          <a className={styles.link}>about</a>
        </Link>
        <Link href="/blog">
          <a className={styles.link}>blog</a>
        </Link>
        <Link href="/contact">
          <a className={styles.link}>contact</a>
        </Link>
      </div>
    </header>
  )
}

export default Header