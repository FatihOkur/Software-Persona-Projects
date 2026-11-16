# ✈ Uçuş Rötar Tahmini — Uçtan Uca Yapay Zeka Projesi: Veriden Tahmine

**Yapay Zeka İçin Basitleştirilmiş Python · Fatih Okur · 2026**

[![Colab'da Aç](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/FatihOkur/Software-Persona-Projects/blob/main/01-Basitlestirilmis-Python/ucus_rotar_tahmini.ipynb)

Uçuş bilgilerinden (hava durumu, görüş, rüzgâr, yoğunluk, önceki uçuş gecikmesi, saat) 15 dakikayı aşan rötarı tahmin eden karar ağacı modeli ve etkileşimli "Rötar Asistanı".

| Dosya | İçerik |
|---|---|
| `ucus_rotar_tahmini.ipynb` | Colab not defteri, Aşama 1–7 (yorumlu, çıktılı) |
| `ucus_rotar_verisi.csv` | 161 satırlık simülasyon veri seti (temizlik pratiği için kirli kayıtlar içerir) |
| `veri_olustur.py` | Veri setini üreten betik |
| `grafikler/` | 6 etiketli grafik |
| `rapor/envanter.pdf` | Proje envanteri + 1 sayfalık proje raporu |
| `rapor/sunum.pptx` | 5 slaytlık sunum |

**Sonuç:** Test doğruluğu %82,5 (temel tahmin %65); rötarlı uçuşların %71'i yakalandı. En belirleyici özellik görüş mesafesi.
