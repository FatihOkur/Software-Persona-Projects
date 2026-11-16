"""
Uçuş Rötar Tahmini — veri seti oluşturma betiği
------------------------------------------------
Bu betik, havacılıkta rötarı etkileyen bilinen faktörlerden (hava durumu,
rüzgâr, görüş mesafesi, havalimanı yoğunluğu, önceki uçuşun gecikmesi,
kalkış saati) yola çıkarak 160 satırlık bir SİMÜLASYON veri seti üretir.

Gerçek bir havayolu verisi DEĞİLDİR; eğitim amaçlı, kurallı ve gürültülü
olarak oluşturulmuştur. Temizleme adımlarını gösterebilmek için bilinçli olarak
birkaç eksik değer, bir hatalı (negatif) değer ve bir tekrar eden satır eklenir.
"""
import numpy as np
import pandas as pd

rng = np.random.default_rng(42)
N = 160

gunler = ["Pzt", "Sal", "Çar", "Per", "Cum", "Cmt", "Paz"]
hava_tipleri = ["Açık", "Bulutlu", "Yağmurlu", "Sisli", "Karlı"]
hava_olasilik = [0.40, 0.27, 0.17, 0.09, 0.07]

satirlar = []
for i in range(N):
    gun = rng.choice(gunler)
    kalkis_saati = int(rng.integers(5, 24))
    hava = rng.choice(hava_tipleri, p=hava_olasilik)

    # Hava durumuna göre rüzgâr ve görüş mesafesi
    ruzgar = {"Açık": 8, "Bulutlu": 12, "Yağmurlu": 18, "Sisli": 6, "Karlı": 22}[hava]
    ruzgar_hizi = max(0, round(rng.normal(ruzgar, 5)))
    gorus = {"Açık": 10, "Bulutlu": 8, "Yağmurlu": 5, "Sisli": 1.2, "Karlı": 2.5}[hava]
    gorus_mesafesi = round(float(np.clip(rng.normal(gorus, gorus * 0.25), 0.2, 10)), 1)

    # Akşam saatleri ve hafta sonu öncesi daha yoğun
    yogunluk = 20 + (12 if 16 <= kalkis_saati <= 20 else 0) + (6 if gun in ["Cum", "Paz"] else 0)
    havalimani_yogunlugu = int(max(5, rng.normal(yogunluk, 6)))

    onceki_ucus_rotari = int(max(0, rng.exponential(10)))
    mesafe_km = int(rng.choice([350, 480, 560, 690, 830, 1050, 1350, 1900, 2400]))

    # Rötar skoru (gizli kural) + gürültü
    skor = (
        0.09 * ruzgar_hizi
        - 0.25 * gorus_mesafesi
        + 0.055 * havalimani_yogunlugu
        + 0.07 * onceki_ucus_rotari
        + (0.6 if kalkis_saati >= 17 else 0)
        + {"Açık": 0, "Bulutlu": 0.2, "Yağmurlu": 0.8, "Sisli": 1.4, "Karlı": 1.6}[hava]
        - 2.6
        + rng.normal(0, 0.6)
    )
    rotar = int(skor > 0)

    satirlar.append({
        "ucus_no": f"SK{1000 + i}",
        "gun": gun,
        "kalkis_saati": kalkis_saati,
        "hava_durumu": hava,
        "ruzgar_hizi": ruzgar_hizi,
        "gorus_mesafesi": gorus_mesafesi,
        "havalimani_yogunlugu": havalimani_yogunlugu,
        "onceki_ucus_rotari": onceki_ucus_rotari,
        "mesafe_km": mesafe_km,
        "rotar": rotar,
    })

df = pd.DataFrame(satirlar)

# --- Temizleme adımlarını göstermek için bilinçli "kirli" veri ---
df.loc[[7, 41, 88], "ruzgar_hizi"] = np.nan          # eksik rüzgâr ölçümü
df.loc[[15, 120], "gorus_mesafesi"] = np.nan          # eksik görüş ölçümü
df.loc[63, "hava_durumu"] = np.nan                    # hava durumu kaydı yok
df.loc[102, "ruzgar_hizi"] = -5                       # sensör hatası (negatif)
df = pd.concat([df, df.iloc[[30]]], ignore_index=True)  # tekrar eden satır

df.to_csv("ucus_rotar_verisi.csv", index=False, encoding="utf-8")
print(df.shape)
print(df["rotar"].value_counts())
