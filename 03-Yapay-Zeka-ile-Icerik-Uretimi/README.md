# 📣 SkyTrack Marka İçerik Sistemi — Yapay Zeka ile İçerik Üretimi

**Fatih Okur · 2026** · 🔗 **Sunum (tüm teslim belgeleri tek bağlantıda):** https://fatihokur.github.io/Software-Persona-Projects/icerik/

Kurgusal seyahat teknolojisi markası **SkyTrack** (Web Geliştirme projesindeki uygulama) için yapay zeka araçlarıyla kurulmuş içerik üretim sistemi.

| Teslim çıktısı | Konum |
|---|---|
| Marka Stratejisi Dokümanı (analiz, kimlik kartı, ses rehberi, personalar, içerik sütunları) | Sunum · Aşama 1–2 |
| İçerik Takvimi (7 gün, Excel) | [`sunum/medya/SkyTrack_Icerik_Takvimi.xlsx`](sunum/medya/SkyTrack_Icerik_Takvimi.xlsx) |
| Blog yazısı (SEO) + 3 sosyal medya gönderisi (RTF) | Sunum · Aşama 3 |
| 3 görsel (1080×1080) | [`sunum/medya/`](sunum/medya) |
| 18,5 sn tanıtım videosu (1080×1920) + TTS seslendirme | [`sunum/medya/skytrack_tanitim_videosu.mp4`](sunum/medya/skytrack_tanitim_videosu.mp4) · [`skytrack_seslendirme.mp3`](sunum/medya/skytrack_seslendirme.mp3) |
| İçerik kontrol listesi, AI kullanım raporu, prompt kütüphanesi | Sunum · Aşama 4 |

**Görseller:** Google Gemini ile metinsiz üretildi (ham çıktılar: [`sunum/medya/gemini_ham/`](sunum/medya/gemini_ham)); Türkçe başlık ve logo katmanı `uretim/gorsel_bindir.py` ile eklendi.

**Üretim betikleri** (`uretim/`): `gorsel_bindir.py` (Gemini görseli + metin katmanı), `gorsel_uret.py` (video sahneleri, HTML/CSS → PNG), `video_uret.py` (ffmpeg montaj), `takvim_uret.py` (openpyxl), `seslendirme_metni.txt` (edge-tts, tr-TR-EmelNeural).
