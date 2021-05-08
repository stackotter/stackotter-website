import { FunctionComponent } from "react"
import Page from "./page"

type MarkdownPageProps = {
  html: string
}

const MarkdownPage: FunctionComponent<MarkdownPageProps> = ({ html }) => {
  return (
    <Page>
      <div dangerouslySetInnerHTML={{ __html: html }}/>
    </Page>
  )
}

export default MarkdownPage