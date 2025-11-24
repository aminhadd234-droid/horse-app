import Layout from '../components/Layout'
import { useState } from 'react'

export default function Login() {
  const [email, setEmail] = useState('')
  const [pass, setPass] = useState('')
  const submit = (e:any) => { e.preventDefault(); alert('تم ارسال بيانات (محاكاة)') }
  return (
    <Layout title="تسجيل الدخول">
      <h2>تسجيل الدخول</h2>
      <form onSubmit={submit}>
        <label>البريد<br/>
          <input value={email} onChange={e=>setEmail(e.target.value)} />
        </label><br/>
        <label>كلمة المرور<br/>
          <input type="password" value={pass} onChange={e=>setPass(e.target.value)} />
        </label><br/><br/>
        <button type="submit">دخول</button>
      </form>
    </Layout>
  )
}
