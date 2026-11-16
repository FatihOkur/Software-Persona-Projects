import FlightCard from './FlightCard'

const TABS = [
  { key: 'upcoming', label: 'Yaklaşan' },
  { key: 'past', label: 'Geçmiş' },
  { key: 'all', label: 'Tümü' },
]

// Filtre sekmeleri, arama kutusu ve uçuş kartları
export default function FlightList({ flights, allCount, filter, setFilter, query, setQuery, selectedId, onSelect, onRemove, onUpdate }) {
  return (
    <div className="card list">
      <div className="list-head">
        <div className="tabs" role="tablist">
          {TABS.map((t) => (
            <button
              key={t.key}
              role="tab"
              aria-selected={filter === t.key}
              className={filter === t.key ? 'tab active' : 'tab'}
              onClick={() => setFilter(t.key)}
            >
              {t.label}
            </button>
          ))}
        </div>
        <input
          className="search"
          placeholder="🔍 Şehir kodu, havayolu, not ara..."
          value={query}
          onChange={(e) => setQuery(e.target.value)}
        />
      </div>

      {flights.length === 0 ? (
        <div className="empty">
          <span>🛫</span>
          <p>{allCount === 0 ? 'Henüz uçuş eklemedin. Soldaki formdan ilk uçuşunu ekle!' : 'Bu filtrede uçuş bulunamadı.'}</p>
        </div>
      ) : (
        <ul className="flights">
          {flights.map((f) => (
            <FlightCard
              key={f.id}
              flight={f}
              selected={f.id === selectedId}
              onSelect={() => onSelect(f.id === selectedId ? null : f.id)}
              onRemove={() => onRemove(f.id)}
              onUpdate={(patch) => onUpdate(f.id, patch)}
            />
          ))}
        </ul>
      )}
    </div>
  )
}
