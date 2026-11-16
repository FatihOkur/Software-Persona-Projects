import { AIRPORT_BY_CODE } from '../data/airports'
import { countdownLabel, isUpcoming } from '../utils/flight'

// Üstteki özet kartları: toplam uçuş, mesafe, şehir sayısı ve sıradaki uçuş
export default function StatsBar({ flights, totalKm }) {
  const upcoming = flights.filter((f) => isUpcoming(f))
  const next = upcoming[0]
  const cities = new Set(flights.flatMap((f) => [AIRPORT_BY_CODE[f.from]?.city, AIRPORT_BY_CODE[f.to]?.city]))
  const earthLaps = (totalKm / 40075).toLocaleString('tr-TR', { maximumFractionDigits: 2 })

  return (
    <section className="stats">
      <div className="stat highlight">
        <span className="label">Sıradaki uçuş</span>
        {next ? (
          <>
            <strong>{next.from} → {next.to}</strong>
            <span className="hint">{countdownLabel(next)} · {next.time}</span>
          </>
        ) : (
          <>
            <strong>—</strong>
            <span className="hint">Planlı uçuş yok</span>
          </>
        )}
      </div>
      <div className="stat">
        <span className="label">Toplam uçuş</span>
        <strong>{flights.length}</strong>
        <span className="hint">{upcoming.length} yaklaşan</span>
      </div>
      <div className="stat">
        <span className="label">Toplam mesafe</span>
        <strong>{totalKm.toLocaleString('tr-TR')} km</strong>
        <span className="hint">Dünya çevresinin {earthLaps} katı</span>
      </div>
      <div className="stat">
        <span className="label">Şehir</span>
        <strong>{cities.size}</strong>
        <span className="hint">farklı şehir</span>
      </div>
    </section>
  )
}
