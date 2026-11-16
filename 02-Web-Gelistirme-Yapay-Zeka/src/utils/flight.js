import { AIRPORT_BY_CODE } from '../data/airports'

// İki havalimanı arasındaki büyük daire mesafesi (Haversine formülü), km
export function distanceKm(fromCode, toCode) {
  const a = AIRPORT_BY_CODE[fromCode]
  const b = AIRPORT_BY_CODE[toCode]
  if (!a || !b) return 0
  const R = 6371
  const rad = (d) => (d * Math.PI) / 180
  const dLat = rad(b.lat - a.lat)
  const dLon = rad(b.lon - a.lon)
  const h = Math.sin(dLat / 2) ** 2 + Math.cos(rad(a.lat)) * Math.cos(rad(b.lat)) * Math.sin(dLon / 2) ** 2
  return Math.round(2 * R * Math.asin(Math.sqrt(h)))
}

// Tahmini uçuş süresi: ortalama 780 km/sa seyir + 25 dk kalkış/iniş payı
export function estimateDuration(km) {
  const minutes = Math.round((km / 780) * 60 + 25)
  const h = Math.floor(minutes / 60)
  const m = minutes % 60
  return h > 0 ? `${h} sa ${m} dk` : `${m} dk`
}

export function flightDateTime(flight) {
  return new Date(`${flight.date}T${flight.time || '00:00'}`)
}

// "3 gün kaldı", "Bugün", "12 gün önce" gibi okunur geri sayım
export function countdownLabel(flight, now = new Date()) {
  const start = new Date(now.getFullYear(), now.getMonth(), now.getDate())
  const d = flightDateTime(flight)
  const day = new Date(d.getFullYear(), d.getMonth(), d.getDate())
  const diff = Math.round((day - start) / 86400000)
  if (diff === 0) return 'Bugün'
  if (diff === 1) return 'Yarın'
  if (diff > 1) return `${diff} gün kaldı`
  return `${Math.abs(diff)} gün önce`
}

export function isUpcoming(flight, now = new Date()) {
  return flightDateTime(flight) >= now
}

export function isInternational(flight) {
  const a = AIRPORT_BY_CODE[flight.from]
  const b = AIRPORT_BY_CODE[flight.to]
  return a && b && (a.country !== 'TR' || b.country !== 'TR')
}

export function formatDate(flight) {
  return flightDateTime(flight).toLocaleDateString('tr-TR', {
    day: 'numeric', month: 'long', year: 'numeric', weekday: 'short',
  })
}

// Yeni uçuş için varsayılan kontrol listesi (yurt dışı uçuşlarda pasaport eklenir)
export function defaultChecklist(international) {
  const items = [
    'Online check-in yap',
    'Biniş kartını telefona kaydet',
    'Bagaj ağırlığını kontrol et',
    'Havalimanı ulaşımını planla',
    'Şarj aleti ve powerbank',
  ]
  if (international) items.splice(1, 0, 'Pasaport / vize kontrolü')
  return items.map((text, i) => ({ id: `${Date.now()}-${i}`, text, done: false }))
}

export const uid = () => (crypto.randomUUID ? crypto.randomUUID() : `${Date.now()}-${Math.random()}`)
