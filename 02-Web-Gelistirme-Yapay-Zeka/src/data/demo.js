import { defaultChecklist, isInternational, uid } from '../utils/flight'

// İlk ziyarette gösterilen örnek uçuşlar (tarihler bugüne göre hesaplanır)
function dayOffset(days) {
  const d = new Date()
  d.setDate(d.getDate() + days)
  return d.toISOString().slice(0, 10)
}

function make(from, to, days, time, airline, flightNo, note = '', doneCount = 0) {
  const f = { id: uid(), from, to, date: dayOffset(days), time, airline, flightNo, note }
  const checklist = defaultChecklist(isInternational(f))
  checklist.forEach((item, i) => (item.done = i < doneCount))
  return { ...f, checklist }
}

export function demoFlights() {
  return [
    make('IST', 'AMS', 4, '09:35', 'Turkish Airlines', 'TK1951', 'Konferans — dönüşte aktarma yok', 3),
    make('ESB', 'TZX', 11, '07:10', 'AJet', 'VF3122', 'Yayla tatili', 1),
    make('SAW', 'BAK', 26, '22:40', 'Pegasus', 'PC740', ''),
    make('IST', 'FCO', -18, '13:20', 'ITA Airways', 'AZ717', 'Roma hafta sonu', 6),
    make('ADB', 'IST', -45, '18:05', 'Turkish Airlines', 'TK2329', '', 5),
    make('AYT', 'MUC', -90, '11:00', 'SunExpress', 'XQ940', 'Aile ziyareti', 6),
  ]
}
