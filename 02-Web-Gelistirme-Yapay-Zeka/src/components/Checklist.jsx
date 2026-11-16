import { useState } from 'react'
import { uid } from '../utils/flight'

// Uçuşa özel hazırlık kontrol listesi (işaretle, ekle, sil)
export default function Checklist({ items, onChange }) {
  const [text, setText] = useState('')

  const toggle = (id) => onChange(items.map((i) => (i.id === id ? { ...i, done: !i.done } : i)))
  const remove = (id) => onChange(items.filter((i) => i.id !== id))
  const add = (e) => {
    e.preventDefault()
    if (!text.trim()) return
    onChange([...items, { id: uid(), text: text.trim(), done: false }])
    setText('')
  }

  return (
    <div className="checklist">
      <h3>Yolculuk hazırlık listesi</h3>
      <ul>
        {items.map((i) => (
          <li key={i.id} className={i.done ? 'done' : ''}>
            <label>
              <input type="checkbox" checked={i.done} onChange={() => toggle(i.id)} />
              {i.text}
            </label>
            <button className="x" onClick={() => remove(i.id)} aria-label={`${i.text} maddesini sil`}>×</button>
          </li>
        ))}
      </ul>
      <form onSubmit={add} className="add-item">
        <input placeholder="Yeni madde ekle..." value={text} onChange={(e) => setText(e.target.value)} />
        <button type="submit">Ekle</button>
      </form>
    </div>
  )
}
