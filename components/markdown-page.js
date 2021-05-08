import Page from "../components/page"

export default function MarkdownPage({ html }) {
  return (
    <Page>
      <div dangerouslySetInnerHTML={{ __html: html }}/>
    </Page>
  )
}