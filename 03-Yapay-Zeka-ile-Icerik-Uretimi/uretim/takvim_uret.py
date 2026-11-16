"""SkyTrack 7 günlük içerik takvimini Excel (xlsx) olarak üretir."""
import pathlib
from openpyxl import Workbook
from openpyxl.styles import Alignment, Border, Font, PatternFill, Side

CIKTI = pathlib.Path(__file__).resolve().parent.parent / "sunum" / "medya" / "SkyTrack_Icerik_Takvimi.xlsx"

BASLIK = ["Gün", "Tarih", "Saat", "Kanal", "Format", "İçerik Sütunu", "Konu / Başlık",
          "Hedef Kitle & Gerekçe", "CTA", "Üretim (AI aracı)", "Durum"]
TAKVIM = [
    ["Pazartesi", "23.11.2026", "09:00", "Blog + LinkedIn", "Blog yazısı (SEO)", "Kokpitten Bilgi",
     "Rötar Neden Olur? Uçuşunu Etkileyen 4 Faktör ve Hazırlıklı Olmanın 5 Yolu",
     "Persona Deniz (iş seyahati): haftaya plan yaparak başlar; uzun okuma için hafta başı uygun",
     "Yazının tamamını oku", "Claude (CO-STAR istemi)", "Hazır"],
    ["Salı", "24.11.2026", "12:30", "Instagram", "Görsel gönderi + açıklama", "Kokpitten Bilgi",
     "Rötar neden olur? (4 faktör infografiği)",
     "Her iki persona: öğle arası kısa, kaydırılabilir bilgi; blog trafiğini besler",
     "Biyografideki linkten blogu oku", "Claude (RTF istemi + görsel kodu)", "Hazır"],
    ["Çarşamba", "25.11.2026", "19:00", "Instagram Reels + TikTok", "18 sn dikey video + TTS seslendirme", "SkyTrack'te Bunu Biliyor muydun?",
     "Uçuşun yaklaşıyor mu? SkyTrack tanıtımı",
     "Persona Elif (öğrenci): kısa video tüketimi; akşam saatleri test edilecek varsayım",
     "Ücretsiz dene", "Claude (senaryo) + Edge Neural TTS + ffmpeg", "Hazır"],
    ["Perşembe", "26.11.2026", "08:30", "LinkedIn + X", "Görsel gönderi + metin", "Akıllı Yolcu Rehberi",
     "Havalimanına çıkmadan önce 5 kontrol",
     "Persona Deniz: sabah işe giderken hızlı ipucu; kaydetme/paylaşma potansiyeli yüksek",
     "Listeni SkyTrack'te oluştur", "Claude (RTF istemi + görsel kodu)", "Hazır"],
    ["Cuma", "27.11.2026", "17:00", "Instagram", "Görsel gönderi + açıklama", "SkyTrack'te Bunu Biliyor muydun?",
     "Sıradaki uçuşuna kaç gün kaldığını bil (geri sayım özelliği)",
     "Persona Elif: hafta sonu kaçamağı planlarken; Cuma akşamı tatil modu",
     "Uygulamada geri sayımı başlat", "Claude (RTF istemi + görsel kodu)", "Hazır"],
    ["Cumartesi", "28.11.2026", "11:00", "Instagram Story", "Anket (etkileşim)", "Seyahat Topluluğu",
     "Pencere mi, koridor mu? 🪟✈️🚶",
     "Tüm kitle: hafta sonu düşük eforlu etkileşim; kitle tercihlerini öğrenme",
     "Oy ver", "Claude (soru fikirleri)", "Taslak"],
    ["Pazar", "29.11.2026", "20:00", "E-posta bülteni + LinkedIn", "Haftalık özet", "Seyahat Topluluğu + Ürün",
     "Haftanın özeti: rötar rehberi, 5 kontrol listesi ve yeni JSON dışa aktarma özelliği",
     "Persona Deniz: Pazar akşamı yeni haftanın seyahatlerini planlar",
     "Yaklaşan uçuşlarını ekle", "Claude (özetleme)", "Taslak"],
]

wb = Workbook()
ws = wb.active
ws.title = "7 Günlük Takvim"
ws.append(["SkyTrack — 7 Günlük İçerik Takvimi (23–29 Kasım 2026)"])
ws.merge_cells(start_row=1, start_column=1, end_row=1, end_column=len(BASLIK))
ws["A1"].font = Font(bold=True, size=14, color="FFFFFF")
ws["A1"].fill = PatternFill("solid", fgColor="0B1F3A")
ws["A1"].alignment = Alignment(vertical="center")
ws.row_dimensions[1].height = 28
ws.append(BASLIK)
ince = Side(style="thin", color="D3DEEE")
for c in ws[2]:
    c.font = Font(bold=True, color="0B1F3A")
    c.fill = PatternFill("solid", fgColor="FFB547")
    c.alignment = Alignment(horizontal="center", vertical="center", wrap_text=True)
renk = {"Hazır": "D8F3E3", "Taslak": "FFF1D6"}
for satir in TAKVIM:
    ws.append(satir)
    r = ws.max_row
    for c in ws[r]:
        c.alignment = Alignment(vertical="top", wrap_text=True)
        c.border = Border(top=ince, bottom=ince, left=ince, right=ince)
    ws.cell(r, len(BASLIK)).fill = PatternFill("solid", fgColor=renk[satir[-1]])
    ws.row_dimensions[r].height = 62
for i, w in enumerate([11, 11, 7, 18, 20, 20, 36, 40, 22, 26, 9], 1):
    ws.column_dimensions[chr(64 + i)].width = w
ws.freeze_panes = "A3"

ws2 = wb.create_sheet("İçerik Sütunları")
ws2.append(["İçerik Sütunu", "Amaç", "Haftalık pay", "Örnek"])
for c in ws2[1]:
    c.font = Font(bold=True, color="FFFFFF"); c.fill = PatternFill("solid", fgColor="0B1F3A")
for s in [["Akıllı Yolcu Rehberi", "Pratik hazırlık bilgisi ile güven kazanmak", "%30", "Havalimanına çıkmadan 5 kontrol"],
          ["Kokpitten Bilgi", "Havacılık merakını eğitici içerikle beslemek", "%25", "Rötar neden olur?"],
          ["SkyTrack'te Bunu Biliyor muydun?", "Ürün özelliklerini fayda diliyle tanıtmak", "%30", "Geri sayım, rota haritası"],
          ["Seyahat Topluluğu", "Etkileşim ve kitle tanıma", "%15", "Pencere mi koridor mu? anketi"]]:
    ws2.append(s)
for i, w in enumerate([32, 46, 14, 34], 1):
    ws2.column_dimensions[chr(64 + i)].width = w

wb.save(CIKTI)
print("Kaydedildi:", CIKTI)
