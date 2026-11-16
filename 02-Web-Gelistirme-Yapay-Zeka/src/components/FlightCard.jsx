import { AIRPORT_BY_CODE } from '../data/airports'
import { countdownLabel, distanceKm, estimateDuration, formatDate, isUpcoming } from '../utils/flight'
import Checklist from './Checklist'

// Tek bir uçuşun kartı: rota, tarih, mesafe, geri sayım ve hazırlık listesi
export default function FlightCard({ flight, selected, onSelect, onRemove, onUpdate }) {
  const from = AIRPORT_BY_CODE[flight.from]
  const to = AIRPORT_BY_CODE[flight.to]
  const km = distanceKm(flight.from, flight.to)
  const upcoming = isUpcoming(flight)
  const done = flight.checklist?.filter((c) => c.done).length ?? 0
  const total = flight.checklist?.length ?? 0
  const pct = total ? Math.round((done / total) * 100) : 0

  return (
    <li className={`flight ${selected ? 'selected' : ''} ${upcoming ? '' : 'past'}`}>
      <div className="flight-main" onClick={onSelect} role="button" tabIndex={0}
        onKeyDown={(e) => e.key === 'Enter' && onSelect()}>
        <div className="route">
          <div>
            <b>{flight.from}</b>
            <small>{from?.city}</small>
          </div>
          <div className="path">
            <span className="line" />
            <span className="plane">✈</span>
            <small>{km.toLocaleString('tr-TR')} km · {estimateDuration(km)}</small>
          </div>
          <div>
            <b>{flight.to}</b>
            <small>{to?.city}</small>
          </div>
        </div>
        <div className="meta-row">
          <span>📅 {formatDate(flight)} · {flight.time}</span>
          <span>🛩 {flight.airline}{flight.flightNo && ` · ${flight.flightNo}`}</span>
          <span className={`badge ${upcoming ? 'soon' : 'done'}`}>{countdownLabel(flight)}</span>
        </div>
        {flight.note && <p className="note">📝 {flight.note}</p>}
        {upcoming && total > 0 && (
          <div className="progress" title={`Hazırlık: ${done}/${total}`}>
            <span style={{ width: `${pct}%` }} />
            <em>Hazırlık %{pct}</em>
          </div>
        )}
      </div>

      {selected && (
        <div className="flight-detail">
          <Checklist items={flight.checklist ?? []} onChange={(checklist) => onUpdate({ checklist })} />
          <button className="link danger" onClick={() => confirm('Bu uçuş silinsin mi?') && onRemove()}>
            🗑 Uçuşu sil
          </button>
        </div>
      )}
    </li>
  )
}
