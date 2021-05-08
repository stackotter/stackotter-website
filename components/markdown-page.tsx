import { FunctionComponent } from "react"
import Page from "./page"
import "github-markdown-css"
import styles from "../styles/page.module.css"

type MarkdownPageProps = {
  html: string
}

const MarkdownPage: FunctionComponent<MarkdownPageProps> = ({ html }) => {
  return (
    <Page>
      <div className={["markdown-body", styles.markdown_body].join(" ")} dangerouslySetInnerHTML={{ __html: html }}/>
    </Page>
  )
}

export default MarkdownPage