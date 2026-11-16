# Software Persona — Yapay Zeka Mesleki Gelişim Programı Proje Portföyü

**Fatih Okur · 2026** · 🌐 Portföy sitesi: https://fatihokur.github.io/Software-Persona-Projects/

| # | Eğitim | Proje | Bağlantılar |
|---|---|---|---|
| 1 | Basitleştirilmiş Python | ✈ Uçuş Rötar Tahmini — veriden tahmine uçtan uca karar ağacı projesi | [Colab](https://colab.research.google.com/github/FatihOkur/Software-Persona-Projects/blob/main/01-Basitlestirilmis-Python/ucus_rotar_tahmini.ipynb) · [Klasör](01-Basitlestirilmis-Python) |
| 2 | Web Geliştirme; Yapay Zeka | 🗺 SkyTrack — React + Vite uçuş planlayıcı (LocalStorage) | [Canlı demo](https://fatihokur.github.io/Software-Persona-Projects/skytrack/) · [Klasör](02-Web-Gelistirme-Yapay-Zeka) |
| 3 | Yapay Zeka ile İçerik Üretimi | 📣 SkyTrack Marka İçerik Sistemi | [Sunum](https://fatihokur.github.io/Software-Persona-Projects/icerik/) · [Klasör](03-Yapay-Zeka-ile-Icerik-Uretimi) |
| 4 | Makine ve Derin Öğrenme Uygulamaları | 🛠 Kestirimci Bakım — LR, Random Forest, PyTorch MLP | [Colab](https://colab.research.google.com/github/FatihOkur/Software-Persona-Projects/blob/main/04-Makine-ve-Derin-Ogrenme/kestirimci_bakim.ipynb) · [Klasör](04-Makine-ve-Derin-Ogrenme) |

`Teslim/` klasörü, teslim formuna yüklenen dosyaları eğitim adlarıyla içerir.

## Yeniden üretme
```bash
# 1 — Python projesi
cd 01-Basitlestirilmis-Python && python veri_olustur.py && python notebook_olustur.py
# 2 — Web uygulaması
cd 02-Web-Gelistirme-Yapay-Zeka && npm install && npm run dev
# 3 — İçerik: görseller, takvim, video (edge-tts ve imageio-ffmpeg gerekir)
cd 03-Yapay-Zeka-ile-Icerik-Uretimi/uretim && python takvim_uret.py && python video_uret.py
# 4 — ML/DL projesi
cd 04-Makine-ve-Derin-Ogrenme && python notebook_olustur.py
```

Veri kaynağı (Proje 4): AI4I 2020 Predictive Maintenance Dataset, UCI Machine Learning Repository, CC BY 4.0.
Proje 1'deki veri seti, eğitim amaçlı oluşturulmuş bir simülasyondur.
