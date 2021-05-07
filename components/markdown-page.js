import Page from "../components/page"
import "github-markdown-css"
import styles from "../styles/page.module.css"

export default function MarkdownPage({ html }) {
  return (
    <Page>
      <div className={ "markdown-body " + styles.markdown_body } dangerouslySetInnerHTML={{ __html: html }}/>
    </Page>
  )
}