// components
import Header from './header'
import Meta from './meta'

// styles
import styles from '../styles/page.module.css'

export default function Page({ children }) {
  return (
    <div className={styles.container}>
      <Meta/>
      <Header/>
      <main className={styles.main}>
        {children}
      </main>
    </div>
  )
}
