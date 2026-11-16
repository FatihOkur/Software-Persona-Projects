"""5 slaytlık proje sunumunu (PPTX) üreten betik."""
from pptx import Presentation
from pptx.util import Inches, Pt, Emu
from pptx.dml.color import RGBColor
from pptx.enum.shapes import MSO_SHAPE
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR

NAVY = RGBColor(0x1F, 0x3A, 0x5F)
DEEP = RGBColor(0x0F, 0x1B, 0x2D)
ORANGE = RGBColor(0xE4, 0x57, 0x2E)
GREEN = RGBColor(0x6B, 0xAA, 0x3E)
INK = RGBColor(0x1D, 0x24, 0x33)
MUTED = RGBColor(0x5B, 0x65, 0x78)
SOFT = RGBColor(0xF3, 0xF6, 0xFA)
WHITE = RGBColor(0xFF, 0xFF, 0xFF)
FONT = "Segoe UI"
G = "../grafikler/"

prs = Presentation()
prs.slide_width, prs.slide_height = Inches(13.333), Inches(7.5)
BLANK = prs.slide_layouts[6]


def rect(slide, x, y, w, h, fill, line=None, shape=MSO_SHAPE.RECTANGLE):
    s = slide.shapes.add_shape(shape, x, y, w, h)
    s.fill.solid(); s.fill.fore_color.rgb = fill
    if line is None:
        s.line.fill.background()
    else:
        s.line.color.rgb = line
    s.shadow.inherit = False
    return s


def text(slide, x, y, w, h, runs, size=16, color=INK, bold=False, align=PP_ALIGN.LEFT, anchor=MSO_ANCHOR.TOP):
    """runs: str veya [(metin, {bold, color, size}) ...] satır listesi"""
    tb = slide.shapes.add_textbox(x, y, w, h)
    tf = tb.text_frame; tf.word_wrap = True; tf.vertical_anchor = anchor
    tf.margin_left = tf.margin_right = Inches(0.05)
    lines = runs if isinstance(runs, list) else [runs]
    for i, line in enumerate(lines):
        p = tf.paragraphs[0] if i == 0 else tf.add_paragraph()
        p.alignment = align
        p.space_after = Pt(6)
        parts = line if isinstance(line, list) else [(line, {})]
        for t, st in parts:
            r = p.add_run(); r.text = t
            r.font.name = FONT; r.font.size = Pt(st.get("size", size))
            r.font.bold = st.get("bold", bold); r.font.color.rgb = st.get("color", color)
    return tb


def header(slide, kicker, title, no):
    rect(slide, 0, 0, prs.slide_width, Inches(1.25), NAVY)
    rect(slide, 0, Inches(1.25), prs.slide_width, Inches(0.06), ORANGE)
    text(slide, Inches(0.6), Inches(0.18), Inches(10), Inches(0.4), kicker.upper(), size=12, color=RGBColor(0xFF, 0xB5, 0x47), bold=True)
    text(slide, Inches(0.6), Inches(0.5), Inches(11.5), Inches(0.7), title, size=28, color=WHITE, bold=True)
    text(slide, Inches(0.6), Inches(7.0), Inches(9), Inches(0.35),
         "Fatih Okur · Yapay Zeka İçin Basitleştirilmiş Python · Uçuş Rötar Tahmini", size=10, color=MUTED)
    text(slide, Inches(12.0), Inches(7.0), Inches(0.8), Inches(0.35), f"{no} / 5", size=10, color=MUTED, align=PP_ALIGN.RIGHT)


def card(slide, x, y, w, h, title, body, accent=NAVY, size=14):
    rect(slide, x, y, w, h, SOFT)
    rect(slide, x, y, Inches(0.08), h, accent)
    text(slide, x + Inches(0.25), y + Inches(0.12), w - Inches(0.35), Inches(0.4), title, size=15, color=accent, bold=True)
    text(slide, x + Inches(0.25), y + Inches(0.55), w - Inches(0.35), h - Inches(0.6), body, size=size)


def kpi(slide, x, y, w, value, label, color=NAVY):
    rect(slide, x, y, w, Inches(1.15), WHITE, line=RGBColor(0xD9, 0xDE, 0xE7))
    text(slide, x, y + Inches(0.08), w, Inches(0.6), value, size=30, color=color, bold=True, align=PP_ALIGN.CENTER)
    text(slide, x, y + Inches(0.68), w, Inches(0.4), label, size=11, color=MUTED, align=PP_ALIGN.CENTER)


# ---------------- Slayt 1: Kapak ----------------
s = prs.slides.add_slide(BLANK)
rect(s, 0, 0, prs.slide_width, prs.slide_height, DEEP)
rect(s, 0, Inches(5.9), prs.slide_width, Inches(0.06), ORANGE)
text(s, Inches(0.8), Inches(0.8), Inches(11), Inches(0.5), "YAPAY ZEKA İÇİN BASİTLEŞTİRİLMİŞ PYTHON · PROJE SUNUMU",
     size=14, color=RGBColor(0xFF, 0xB5, 0x47), bold=True)
text(s, Inches(0.8), Inches(1.5), Inches(11.5), Inches(1.2), "✈ Uçuş Rötar Tahmini", size=54, color=WHITE, bold=True)
text(s, Inches(0.8), Inches(2.65), Inches(11.5), Inches(0.6), "Uçtan Uca Yapay Zeka Projesi: Veriden Tahmine",
     size=24, color=RGBColor(0xC9, 0xD6, 0xE8))
text(s, Inches(0.8), Inches(3.55), Inches(11.5), Inches(1.2),
     [[("Problem: ", {"bold": True, "color": RGBColor(0xFF, 0xB5, 0x47)}),
       ("Bir uçuşun hava durumu, görüş mesafesi, yoğunluk ve önceki uçuşun gecikmesi gibi bilgilerinden "
        "15 dakikayı aşan rötar yapıp yapmayacağını tahmin etmek.", {"color": WHITE})]], size=18)
for i, (v, l) in enumerate([("159", "temizlenmiş uçuş kaydı"), ("8", "özellik"), ("%82,5", "test doğruluğu"), ("6", "grafik")]):
    x = Inches(0.8 + i * 2.2)
    text(s, x, Inches(4.6), Inches(2), Inches(0.6), v, size=30, color=WHITE, bold=True)
    text(s, x, Inches(5.2), Inches(2), Inches(0.4), l, size=12, color=RGBColor(0xC9, 0xD6, 0xE8))
text(s, Inches(0.8), Inches(6.2), Inches(11), Inches(0.8),
     [[("Fatih Okur", {"bold": True, "color": WHITE, "size": 16})],
      [("Software Persona Yapay Zeka Mesleki Gelişim Programı · 2026", {"color": RGBColor(0xC9, 0xD6, 0xE8), "size": 12})]])

# ---------------- Slayt 2: Problem ve Veri ----------------
s = prs.slides.add_slide(BLANK)
header(s, "Problem & Veri", "Neyi tahmin ediyoruz, hangi veriyle?", 2)
card(s, Inches(0.6), Inches(1.6), Inches(5.9), Inches(2.45), "Proje Tanım Formu", [
    [("Soru: ", {"bold": True}), ("Uçuş bilgilerinden 15 dk üzeri rötar olacak mı?", {})],
    [("Hedef (y): ", {"bold": True}), ("rotar → 1 = Rötarlı, 0 = Zamanında", {})],
    [("Tür: ", {"bold": True}), ("Sınıflandırma (ikili)", {})],
    [("Kime faydalı: ", {"bold": True}), ("Yolcu (erken uyarı), havayolu (yedek planlama), havalimanı (kapı/pist planı)", {})],
], size=13)
card(s, Inches(0.6), Inches(4.25), Inches(5.9), Inches(2.55), "Veri Seti", [
    "Tarafımca Python ile üretilen 161 satırlık simülasyon verisi (gerçek havayolu verisi değildir).",
    "8 özellik: kalkış saati, gün, hava durumu, rüzgâr, görüş mesafesi, havalimanı yoğunluğu, önceki uçuş gecikmesi, mesafe.",
    "Hedef dağılımı: 102 zamanında / 57 rötarlı (%35,8).",
], accent=GREEN, size=13)
card(s, Inches(6.8), Inches(1.6), Inches(5.9), Inches(5.2), "Veri Temizleme (Pandas)", [
    [("✔ ", {"color": GREEN, "bold": True}), ("1 tekrar eden satır → drop_duplicates()", {})],
    [("✔ ", {"color": GREEN, "bold": True}), ("1 negatif rüzgâr (sensör hatası) → NaN", {})],
    [("✔ ", {"color": GREEN, "bold": True}), ("4 eksik rüzgâr → fillna(medyan)", {})],
    [("✔ ", {"color": GREEN, "bold": True}), ("2 eksik görüş → aynı hava koşulunun medyanı", {})],
    [("✔ ", {"color": GREEN, "bold": True}), ("1 eksik hava durumu → dropna()", {})],
    "",
    [("Sonuç: ", {"bold": True, "color": NAVY}), ("161 → 159 satır, 0 eksik değer", {"bold": True})],
    "",
    [("Araçlar: ", {"bold": True, "color": NAVY}), ("Python · Google Colab · Pandas · NumPy · Matplotlib · scikit-learn", {})],
], accent=ORANGE, size=14)

# ---------------- Slayt 3: Keşif (en önemli grafik) ----------------
s = prs.slides.add_slide(BLANK)
header(s, "Keşifçi Veri Analizi", "Kötü görüş = rötar: hava durumu en güçlü sinyal", 3)
s.shapes.add_picture(G + "1_hava_durumu_rotar.png", Inches(0.6), Inches(1.6), width=Inches(7.3))
card(s, Inches(8.2), Inches(1.6), Inches(4.5), Inches(5.2), "Keşif Bulguları", [
    [("❄ Kar %100, sis %80, yağmur %62 ", {"bold": True}), ("rötar oranı; açık havada yalnızca %9.", {})],
    [("👁 Görüş: ", {"bold": True}), ("rötarlılarda ort. 3,8 km, zamanındakilerde 8,4 km.", {})],
    [("⛓ Zincirleme gecikme: ", {"bold": True}), ("önceki uçuş gecikmesi 12,8 dk'ya karşı 8,2 dk.", {})],
    [("🌆 Akşam (17–20): ", {"bold": True}), ("%53 rötar; sabah %27.", {})],
    [("⚠ Mesafe farkı tesadüf: ", {"bold": True}), ("korelasyon nedensellik değildir.", {})],
], accent=ORANGE, size=13)

# ---------------- Slayt 4: Yöntem ve Sonuç ----------------
s = prs.slides.add_slide(BLANK)
header(s, "Yöntem & Sonuç", "Karar ağacı %82,5 doğrulukla rötarı tahmin ediyor", 4)
kpi(s, Inches(0.6), Inches(1.6), Inches(2.0), "%82,5", "Test doğruluğu", GREEN)
kpi(s, Inches(2.75), Inches(1.6), Inches(2.0), "%65,0", "Temel tahmin", MUTED)
kpi(s, Inches(4.9), Inches(1.6), Inches(2.0), "10/14", "Yakalanan rötar", ORANGE)
card(s, Inches(0.6), Inches(2.95), Inches(6.3), Inches(3.85), "Nasıl kuruldu?", [
    "• %75 eğitim / %25 test (stratify) → X_train (119, 8), X_test (40, 8)",
    "• Model: DecisionTreeClassifier(max_depth=3, min_samples_leaf=5)",
    "• Derinlik, test verisine bakmadan 5×10 tekrarlı çapraz doğrulama ile seçildi; derin ağaçlar sadece ezberliyor",
    "• Neden karar ağacı? İnsanın okuyabildiği kurallar, ölçeklendirme gerekmez",
    [("Karmaşıklık matrisi: ", {"bold": True}), ("23 doğru zamanında, 10 doğru rötarlı, 3 yanlış alarm, 4 kaçırılan rötar", {})],
], size=13)
s.shapes.add_picture(G + "5_ozellik_onemi.png", Inches(7.2), Inches(1.6), width=Inches(5.5))
text(s, Inches(7.2), Inches(5.35), Inches(5.5), Inches(1.4), [
    [("Not: ", {"bold": True, "color": ORANGE}), ("Model kararının %89'unu görüş mesafesine dayandırıyor. "
      "Test kümesi küçük (40 uçuş), veri simülasyon; gerçek veriyle doğrulanmalı.", {})]], size=12, color=MUTED)

# ---------------- Slayt 5: Mini uygulama ve çıkarım ----------------
s = prs.slides.add_slide(BLANK)
header(s, "Akıllı Tahmin Aracı & Çıkarım", "Tahmini okunur bir cümleye çeviren mini uygulama", 5)
box = rect(s, Inches(0.6), Inches(1.6), Inches(7.2), Inches(3.0), DEEP)
text(s, Inches(0.8), Inches(1.75), Inches(6.9), Inches(2.8), [
    [("=== SkyTrack Rötar Asistanı ===", {"color": RGBColor(0xFF, 0xB5, 0x47), "bold": True})],
    [("Kalkış: 19:00 | Gün: Paz | Hava: Karlı | Görüş: 2.0 km", {"color": RGBColor(0xC9, 0xD6, 0xE8)})],
    [("✈ Rötar riski %100 → YÜKSEK. Aktarmanız varsa havayolunuzla iletişime geçin ve alternatif planlayın.", {"color": WHITE})],
    [("✈ Salı 07:00, açık hava → rötar riski %0 → DÜŞÜK. İyi yolculuklar!", {"color": WHITE})],
], size=14)
text(s, Inches(0.6), Inches(4.75), Inches(7.2), Inches(2.0), [
    [("tahmin_et()", {"bold": True, "color": NAVY}), (" fonksiyonu modelin olasılığını DÜŞÜK / ORTA / YÜKSEK risk seviyesine çevirir ve öneri verir.", {})],
    [("ucus_asistani()", {"bold": True, "color": NAVY}), (" fonksiyonu input() ile 8 bilgi alır ve sonucu f-string ile yazdırır.", {})],
], size=14)
card(s, Inches(8.1), Inches(1.6), Inches(4.6), Inches(5.2), "Çıkarım & Sonraki Adımlar", [
    [("Kötü görüş ve akşam yoğunluğu ", {"bold": True}), ("rötarın en güçlü habercileri.", {})],
    "Basit ve açıklanabilir bir model bile anlamlı bir erken uyarı sağlıyor.",
    [("Sonraki adımlar: ", {"bold": True, "color": ORANGE}), ("gerçek uçuş + METAR verisi, Random Forest, class_weight ile kaçırılan rötarları azaltmak.", {})],
    "",
    [("Colab: ", {"bold": True}), ("github.com/FatihOkur/Software-Persona-Projects → 01-Basitlestirilmis-Python", {"size": 11})],
], accent=GREEN, size=13)

prs.save("sunum.pptx")
print("sunum.pptx kaydedildi")
