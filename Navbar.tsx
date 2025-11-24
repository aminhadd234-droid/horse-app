import Link from 'next/link'
import { useState } from 'react'

export default function Navbar(){
  const [lang, setLang] = useState<'en'|'ar'>('en')
  return (
    <header style={{display:'flex',gap:20,alignItems:'center',padding:10,borderBottom:'1px solid #ddd'}}>
      <div style={{fontWeight:700}}>MyApp</div>
      <nav style={{display:'flex',gap:12}}>
        <Link href='/'>Home</Link>
        <Link href='/dashboard'>Dashboard</Link>
        <Link href='/login'>Login</Link>
      </nav>
      <div style={{marginLeft:'auto'}}>
        <button onClick={()=>setLang(l=>l==='en'?'ar':'en')}>Lang: {lang}</button>
      </div>
    </header>
  )
}
