// components
import Header from './header'
import Meta from './meta'
import { FunctionComponent } from 'react'

// styles
import styles from '../styles/page.module.css'
import 'github-markdown-css'

const Page: FunctionComponent = ({ children }) => {
  return (
    <div className={styles.container}>
      <Meta />
      <Header />
      <main className={["markdown-body", styles.markdown_body, styles.main].join(" ")}>
        {children}
      </main>
    </div>
  )
}

export default Page