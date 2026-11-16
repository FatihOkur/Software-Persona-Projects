import { useEffect, useMemo, useState } from 'react'
import { useLocalStorage } from './hooks/useLocalStorage'
import { demoFlights } from './data/demo'
import { distanceKm, flightDateTime, isUpcoming } from './utils/flight'
import StatsBar from './components/StatsBar'
import FlightForm from './components/FlightForm'
import FlightList from './components/FlightList'
import RouteMap from './components/RouteMap'

export default function App() {
  // Uçuşlar LocalStorage'da saklanır; ilk ziyarette örnek veriler yüklenir
  const [flights, setFlights] = useLocalStorage('skytrack.flights', demoFlights)
  const [theme, setTheme] = useLocalStorage('skytrack.theme', 'dark')
  const [filter, setFilter] = useState('upcoming')
  const [query, setQuery] = useState('')
  const [selectedId, setSelectedId] = useState(null)

  useEffect(() => {
    document.documentElement.dataset.theme = theme
  }, [theme])

  const sorted = useMemo(
    () => [...flights].sort((a, b) => flightDateTime(a) - flightDateTime(b)),
    [flights],
  )

  const visible = useMemo(() => {
    const q = query.trim().toLocaleLowerCase('tr')
    return sorted
      .filter((f) => (filter === 'all' ? true : filter === 'upcoming' ? isUpcoming(f) : !isUpcoming(f)))
      .filter((f) =>
        !q ||
        [f.from, f.to, f.airline, f.flightNo, f.note].join(' ').toLocaleLowerCase('tr').includes(q),
      )
      // Geçmiş uçuşlarda en yeni en üstte
      .sort((a, b) => (filter === 'past' ? flightDateTime(b) - flightDateTime(a) : 0))
  }, [sorted, filter, query])

  const addFlight = (flight) => {
    setFlights((prev) => [...prev, flight])
    setFilter(isUpcoming(flight) ? 'upcoming' : 'past')
    setSelectedId(flight.id)
  }

  const removeFlight = (id) => setFlights((prev) => prev.filter((f) => f.id !== id))

  const updateFlight = (id, patch) =>
    setFlights((prev) => prev.map((f) => (f.id === id ? { ...f, ...patch } : f)))

  const resetDemo = () => {
    if (confirm('Tüm uçuşlar silinip örnek veriler yüklensin mi?')) setFlights(demoFlights())
  }

  const clearAll = () => {
    if (confirm('Tüm uçuşlar kalıcı olarak silinsin mi?')) setFlights([])
  }

  const exportJson = () => {
    const blob = new Blob([JSON.stringify(flights, null, 2)], { type: 'application/json' })
    const a = document.createElement('a')
    a.href = URL.createObjectURL(blob)
    a.download = 'skytrack-ucuslar.json'
    a.click()
    URL.revokeObjectURL(a.href)
  }

  const totalKm = flights.reduce((sum, f) => sum + distanceKm(f.from, f.to), 0)

  return (
    <div className="app">
      <header className="topbar">
        <div className="brand">
          <span className="logo" aria-hidden>✈</span>
          <div>
            <h1>SkyTrack</h1>
            <p>Uçuşlarını planla, rotalarını gör, yolculuğa hazır ol.</p>
          </div>
        </div>
        <div className="top-actions">
          <button className="ghost" onClick={exportJson} title="Uçuşları JSON olarak indir">⤓ Dışa aktar</button>
          <button
            className="ghost"
            onClick={() => setTheme(theme === 'dark' ? 'light' : 'dark')}
            aria-label="Temayı değiştir"
          >
            {theme === 'dark' ? '☀ Açık tema' : '☾ Koyu tema'}
          </button>
        </div>
      </header>

      <StatsBar flights={sorted} totalKm={totalKm} />

      <main className="grid">
        <section className="col-left">
          <FlightForm onAdd={addFlight} />
          <RouteMap flights={flights} selectedId={selectedId} onSelect={setSelectedId} />
        </section>

        <section className="col-right">
          <FlightList
            flights={visible}
            allCount={flights.length}
            filter={filter}
            setFilter={setFilter}
            query={query}
            setQuery={setQuery}
            selectedId={selectedId}
            onSelect={setSelectedId}
            onRemove={removeFlight}
            onUpdate={updateFlight}
          />
          <div className="footer-actions">
            <button className="link" onClick={resetDemo}>Örnek verileri yükle</button>
            <span>·</span>
            <button className="link danger" onClick={clearAll}>Tümünü temizle</button>
          </div>
        </section>
      </main>

      <footer className="footer">
        SkyTrack · React + Vite · Veriler yalnızca bu tarayıcıda (LocalStorage) saklanır ·
        Fatih Okur · Web Geliştirme; Yapay Zeka Projesi 2026
      </footer>
    </div>
  )
}
