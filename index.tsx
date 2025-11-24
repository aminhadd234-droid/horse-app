import Link from 'next/link'

export default function Home() {
  return (
    <div>
      <h1>Welcome — الصفحة الرئيسية</h1>
      <p>هذا قالب واجهة أمامية بسيط مع دعم ثنائي اللغة لاحقاً.</p>
      <nav>
        <ul>
          <li><Link href='/login'>Login / تسجيل الدخول</Link></li>
          <li><Link href='/dashboard'>Dashboard / لوحة التحكم</Link></li>
        </ul>
      </nav>
    </div>
  )
}
