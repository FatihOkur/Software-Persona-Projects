import { useEffect, useState } from 'react'

// State'i LocalStorage ile senkron tutan özel hook.
// Sayfa yenilense de veriler tarayıcıda saklanır.
export function useLocalStorage(key, initialValue) {
  const [value, setValue] = useState(() => {
    try {
      const saved = localStorage.getItem(key)
      if (saved !== null) return JSON.parse(saved)
    } catch {
      /* gizli sekme veya bozuk veri: varsayılan değere dön */
    }
    return typeof initialValue === 'function' ? initialValue() : initialValue
  })

  useEffect(() => {
    try {
      localStorage.setItem(key, JSON.stringify(value))
    } catch {
      /* depolama dolu veya engelli: uygulama yine de çalışır */
    }
  }, [key, value])

  return [value, setValue]
}
