import Head from 'next/head'
import React from 'react'
type Props = { children: React.ReactNode; title?: string }
export default function Layout({ children, title='تطبيقي' }: Props) {
  return (
    <div style={{ padding: 20, fontFamily: 'Arial, sans-serif' }}>
      <Head>
        <title>{title}</title>
        <meta name="viewport" content="width=device-width, initial-scale=1" />
      </Head>
      <header style={{ borderBottom: '1px solid #ddd', marginBottom: 20 }}>
        <h3>{title}</h3>
      </header>
      <main>{children}</main>
      <footer style={{ marginTop: 40, borderTop: '1px solid #eee', paddingTop: 10 }}>
        <small>واجهة فرونتند — مثال</small>
      </footer>
    </div>
  )
}
