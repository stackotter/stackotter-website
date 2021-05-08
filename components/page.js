// components
import Header from './header'
import Meta from './meta'

// styles
import styles from '../styles/page.module.css'
import 'github-markdown-css'

export default function Page({ children }) {
  return (
    <div className={styles.container}>
      <Meta/>
      <Header/>
      <main className={ ["markdown-body", styles.markdown_body, styles.main].join(" ") }>
        {children}
      </main>
    </div>
  )
}
