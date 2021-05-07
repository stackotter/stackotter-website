import Page from "../components/page"
import styles from "../styles/page.module.css"

export default function MarkdownPage({ html }) {
  return (
    <Page>
      <div className={ "markdown-body " + styles.markdown } dangerouslySetInnerHTML={{ __html: html }}/>
    </Page>
  )
}