import Link from 'next/link'
import Layout from '../components/Layout'

export default function Home() {
  return (
    <Layout title="الصفحة الرئيسية">
      <h1>مرحبا بك في واجهة الفرونتند (Next.js)</h1>
      <p>هذه صفحة رئيسية مبسّطة.</p>
      <nav>
        <ul>
          <li><Link href="/login">تسجيل الدخول</Link></li>
        </ul>
      </nav>
    </Layout>
  )
}
