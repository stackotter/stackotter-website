import styles from '../styles/header.module.css'
import Link from 'next/link'

export default function Header() {
  return (
    <header className={styles.header}>
      <a href="/">
        <img src="/image/otter.png" alt="stackotter logo" className={styles.logo}/>
      </a>

      <h1 className={[styles.serif, styles.h1].join(" ")}>stackotter.dev</h1>

      <div>
        <Link href="/about" className={styles.link}>
          <a>about</a>
        </Link>
        <Link href="/blog" className={styles.link}>
          <a>blog</a>
        </Link>
        <Link href="/contact">
          <a className={styles.link}>contact</a>
        </Link>
      </div>
    </header>
  )
}