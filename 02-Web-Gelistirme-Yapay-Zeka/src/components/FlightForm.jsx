import { useState } from 'react'
import { AIRPORTS } from '../data/airports'
import { defaultChecklist, distanceKm, estimateDuration, isInternational, uid } from '../utils/flight'

const today = () => new Date().toISOString().slice(0, 10)
const EMPTY = { from: 'IST', to: 'ESB', date: today(), time: '10:00', airline: '', flightNo: '', note: '' }

// Yeni uçuş ekleme formu (kontrollü bileşen + doğrulama)
export default function FlightForm({ onAdd }) {
  const [form, setForm] = useState(EMPTY)
  const [error, setError] = useState('')

  const set = (key) => (e) => setForm({ ...form, [key]: e.target.value })
  const km = distanceKm(form.from, form.to)

  const submit = (e) => {
    e.preventDefault()
    if (form.from === form.to) return setError('Kalkış ve varış havalimanı aynı olamaz.')
    if (!form.date) return setError('Lütfen uçuş tarihini seçin.')
    if (form.flightNo && !/^[A-Za-z0-9]{2}\s?\d{1,4}$/.test(form.flightNo.trim()))
      return setError('Uçuş numarası "TK1951" biçiminde olmalı.')

    const flight = {
      ...form,
      id: uid(),
      airline: form.airline.trim() || 'Belirtilmedi',
      flightNo: form.flightNo.trim().toUpperCase().replace(/\s/g, ''),
      note: form.note.trim(),
    }
    flight.checklist = defaultChecklist(isInternational(flight))
    onAdd(flight)
    setForm({ ...EMPTY, date: form.date })
    setError('')
  }

  const swap = () => setForm({ ...form, from: form.to, to: form.from })

  return (
    <form className="card form" onSubmit={submit}>
      <h2>Yeni uçuş ekle</h2>
      <div className="route-row">
        <label>
          Nereden
          <select value={form.from} onChange={set('from')}>
            {AIRPORTS.map((a) => (
              <option key={a.code} value={a.code}>{a.code} · {a.city}</option>
            ))}
          </select>
        </label>
        <button type="button" className="swap" onClick={swap} aria-label="Yönü değiştir">⇄</button>
        <label>
          Nereye
          <select value={form.to} onChange={set('to')}>
            {AIRPORTS.map((a) => (
              <option key={a.code} value={a.code}>{a.code} · {a.city}</option>
            ))}
          </select>
        </label>
      </div>
      <div className="row2">
        <label>Tarih<input type="date" value={form.date} onChange={set('date')} /></label>
        <label>Saat<input type="time" value={form.time} onChange={set('time')} /></label>
      </div>
      <div className="row2">
        <label>Havayolu<input placeholder="Turkish Airlines" value={form.airline} onChange={set('airline')} /></label>
        <label>Uçuş no<input placeholder="TK1951" value={form.flightNo} onChange={set('flightNo')} /></label>
      </div>
      <label>Not<input placeholder="Aktarma, koltuk, otel..." value={form.note} onChange={set('note')} /></label>

      {form.from !== form.to && (
        <p className="preview">
          📏 {km.toLocaleString('tr-TR')} km · ⏱ yaklaşık {estimateDuration(km)}
          {isInternational(form) && ' · 🛂 yurt dışı (pasaport kontrolü eklenecek)'}
        </p>
      )}
      {error && <p className="error" role="alert">{error}</p>}
      <button className="primary" type="submit">+ Uçuşu kaydet</button>
    </form>
  )
}
