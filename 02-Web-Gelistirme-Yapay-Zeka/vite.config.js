import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'

// base: './' → uygulama hangi alt klasörde yayınlanırsa yayınlansın (GitHub Pages, Netlify) çalışır
export default defineConfig({
  plugins: [react()],
  base: './',
})
