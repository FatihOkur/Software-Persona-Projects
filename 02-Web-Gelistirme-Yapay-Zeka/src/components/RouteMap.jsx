import { AIRPORT_BY_CODE } from '../data/airports'
import { isUpcoming } from '../utils/flight'

// Basit eşdikdörtgen projeksiyon: boylam/enlem → SVG koordinatı
// Avrupa–Türkiye–Kafkasya odaklı pencere; dışındaki noktalar kenara sabitlenir
const BOUNDS = { lonMin: -3, lonMax: 52, latMin: 33, latMax: 55 }
const W = 640
const H = 380
const PAD = 18
const clamp = (v, lo, hi) => Math.min(hi, Math.max(lo, v))
const project = ({ lat, lon }) => [
  PAD + ((clamp(lon, BOUNDS.lonMin, BOUNDS.lonMax) - BOUNDS.lonMin) / (BOUNDS.lonMax - BOUNDS.lonMin)) * (W - 2 * PAD),
  PAD + ((BOUNDS.latMax - clamp(lat, BOUNDS.latMin, BOUNDS.latMax)) / (BOUNDS.latMax - BOUNDS.latMin)) * (H - 2 * PAD),
]

// Uçuş rotalarını kavisli çizgilerle gösteren SVG harita
export default function RouteMap({ flights, selectedId, onSelect }) {
  const used = new Set(flights.flatMap((f) => [f.from, f.to]))

  return (
    <div className="card map">
      <div className="map-head">
        <h2>Rota haritası</h2>
        <div className="legend">
          <span><i className="dot up" /> Yaklaşan</span>
          <span><i className="dot past" /> Geçmiş</span>
        </div>
      </div>
      <svg viewBox={`0 0 ${W} ${H}`} role="img" aria-label="Uçuş rotaları haritası">
        {/* enlem / boylam ızgarası */}
        {Array.from({ length: 12 }, (_, i) => (
          <line key={`v${i}`} x1={(i * W) / 11} y1="0" x2={(i * W) / 11} y2={H} className="grid-line" />
        ))}
        {Array.from({ length: 7 }, (_, i) => (
          <line key={`h${i}`} x1="0" y1={(i * H) / 6} x2={W} y2={(i * H) / 6} className="grid-line" />
        ))}

        {flights.map((f) => {
          const a = AIRPORT_BY_CODE[f.from]
          const b = AIRPORT_BY_CODE[f.to]
          if (!a || !b) return null
          const [x1, y1] = project(a)
          const [x2, y2] = project(b)
          const mx = (x1 + x2) / 2
          const my = (y1 + y2) / 2 - Math.hypot(x2 - x1, y2 - y1) * 0.25
          const cls = `route-line ${isUpcoming(f) ? 'up' : 'past'} ${f.id === selectedId ? 'sel' : ''}`
          return (
            <path key={f.id} d={`M${x1},${y1} Q${mx},${my} ${x2},${y2}`} className={cls}
              onClick={() => onSelect(f.id)}>
              <title>{f.from} → {f.to}</title>
            </path>
          )
        })}

        {[...used].map((code) => {
          const ap = AIRPORT_BY_CODE[code]
          if (!ap) return null
          const [x, y] = project(ap)
          return (
            <g key={code} className="airport">
              <circle cx={x} cy={y} r="4.5" />
              <text x={x + 7} y={y - 6}>{code}</text>
            </g>
          )
        })}
      </svg>
    </div>
  )
}
