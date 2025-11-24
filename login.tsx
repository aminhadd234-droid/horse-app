import { useState } from 'react'
import { useRouter } from 'next/router'

export default function Login() {
  const [email, setEmail] = useState('')
  const router = useRouter()
  function submit(e:any){ e.preventDefault(); router.push('/dashboard') }
  return (
    <div style={{maxWidth:480}}>
      <h2>Login — تسجيل الدخول</h2>
      <form onSubmit={submit}>
        <label>Email / البريد الإلكتروني<br/>
          <input value={email} onChange={e=>setEmail(e.target.value)} placeholder="you@example.com" />
        </label>
        <br/><br/>
        <button type="submit">Enter / دخول</button>
      </form>
    </div>
  )
}
