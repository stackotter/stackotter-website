// components
import Header from './header'
import { FunctionComponent } from 'react'

// styles
import styles from '../styles/page.module.css'
import 'github-markdown-css'

const Page: FunctionComponent = ({ children }) => {
  return (
    <div className={styles.container}>
      <Header />
      <main className={["markdown-body", styles.markdown_body, styles.main].join(" ")}>
        {children}
      </main>
    </div>
  )
}

export default Page
