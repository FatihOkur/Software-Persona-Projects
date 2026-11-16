"""
SkyTrack marka görsellerini ve video sahnelerini üretir.
Her görsel, marka paletine bağlı bir HTML/CSS şablonundan Edge (headless) ile PNG olarak alınır.
Kullanım: python gorsel_uret.py <edge.py yolu>
"""
import pathlib, subprocess, sys

EDGE_PY = sys.argv[1]
KOK = pathlib.Path(__file__).resolve().parent
TMP = KOK / "_html"; TMP.mkdir(exist_ok=True)
CIKTI = KOK.parent / "sunum" / "medya"
SAHNE = KOK / "_sahneler"; SAHNE.mkdir(exist_ok=True)
APP_SS = (KOK.parent.parent / "02-Web-Gelistirme-Yapay-Zeka" / "screenshots" / "skytrack-mobile.png").as_uri()

CSS = """
*{box-sizing:border-box;margin:0;padding:0}
body{width:W;height:H;overflow:hidden;font-family:'Segoe UI',sans-serif;color:#E8F0FB;
 background:radial-gradient(900px 700px at 85% 0%,#163a6b,#0B1F3A 55%,#07111f)}
.wrap{position:absolute;inset:0;padding:80px;display:flex;flex-direction:column}
.brand{display:flex;align-items:center;gap:18px;font-weight:800;font-size:38px;letter-spacing:.02em}
.logo{width:68px;height:68px;border-radius:20px;display:grid;place-items:center;font-size:36px;color:#0B1F3A;
 background:linear-gradient(135deg,#FFB547,#ff7a45);transform:rotate(-8deg)}
.kick{color:#FFB547;font-weight:700;letter-spacing:.18em;text-transform:uppercase;font-size:26px}
h1{font-size:84px;line-height:1.05;font-weight:800}
h1 em{font-style:normal;color:#FFB547}
.sub{font-size:34px;color:#B9CCE6;line-height:1.35}
.card{background:rgba(19,48,90,.85);border:2px solid #1f3e6b;border-radius:28px;padding:34px 38px}
.foot{margin-top:auto;display:flex;justify-content:space-between;align-items:center;color:#8ea6c8;font-size:26px}
.dash{height:3px;background:repeating-linear-gradient(90deg,#8ea6c8 0 14px,transparent 14px 26px);flex:1;margin:0 24px}
.pill{display:inline-block;padding:10px 24px;border-radius:99px;font-weight:700;font-size:28px}
"""

def sayfa(w, h, govde):
    return f"<!doctype html><html lang='tr'><head><meta charset='utf-8'><style>{CSS.replace('W', f'{w}px').replace('H', f'{h}px')}</style></head><body>{govde}</body></html>"

BRAND = "<div class='brand'><div class='logo'>✈</div>SkyTrack</div>"

# ---------- 3 sosyal medya görseli (1080x1080) ----------
POSTLAR = {
"gorsel_1_geri_sayim": f"""
<div class='wrap'>{BRAND}
 <div style='margin-top:70px' class='kick'>Sıradaki uçuşun</div>
 <h1 style='margin-top:18px'>Kaç gün<br>kaldığını <em>bil.</em></h1>
 <div class='card' style='margin-top:56px'>
  <div style='display:flex;align-items:center'>
   <div><div style='font-size:76px;font-weight:800'>IST</div><div class='sub' style='font-size:26px'>İstanbul</div></div>
   <div class='dash'></div><div style='font-size:46px;color:#FFB547'>✈</div><div class='dash'></div>
   <div style='text-align:right'><div style='font-size:76px;font-weight:800'>AMS</div><div class='sub' style='font-size:26px'>Amsterdam</div></div>
  </div>
  <div style='display:flex;justify-content:space-between;align-items:center;margin-top:26px'>
   <span class='sub' style='font-size:28px'>2.184 km · ~3 sa 13 dk</span>
   <span class='pill' style='background:rgba(255,181,71,.18);color:#FFB547'>4 gün kaldı</span>
  </div>
 </div>
 <div class='foot'><span>Ücretsiz · Kayıt gerektirmez</span><span style='color:#5AC8FA'>skytrack ↗</span></div>
</div>""",
"gorsel_2_kontrol_listesi": f"""
<div class='wrap'>{BRAND}
 <div style='margin-top:60px' class='kick'>Akıllı yolcu rehberi</div>
 <h1 style='margin-top:16px;font-size:74px'>Havalimanına çıkmadan<br>önce <em>5 kontrol</em></h1>
 <div class='card' style='margin-top:44px;display:grid;gap:20px;font-size:34px'>
  {''.join(f"<div style='display:flex;gap:20px;align-items:center'><span style='width:46px;height:46px;border-radius:12px;display:grid;place-items:center;background:{'#34C77B' if d else 'transparent'};border:3px solid #34C77B;color:#07111f;font-weight:900'>{'✓' if d else ''}</span><span style='{'text-decoration:line-through;color:#8ea6c8' if d else ''}'>{t}</span></div>" for t, d in [("Online check-in", True), ("Kimlik / pasaport", True), ("Biniş kartı telefonda", True), ("Bagaj ağırlığı", False), ("Havalimanı ulaşımı", False)])}
 </div>
 <div class='foot'><span>Hazırlık %60</span><span style='color:#5AC8FA'>Listeni SkyTrack'te tut ↗</span></div>
</div>""",
"gorsel_3_rotar_nedenleri": f"""
<div class='wrap'>{BRAND}
 <div style='margin-top:56px' class='kick'>Kokpitten bilgi</div>
 <h1 style='margin-top:14px;font-size:78px'>Rötar neden olur?</h1>
 <div style='display:grid;grid-template-columns:1fr 1fr;gap:24px;margin-top:44px'>
  {''.join(f"<div class='card' style='padding:28px'><div style='font-size:54px'>{i}</div><div style='font-size:34px;font-weight:800;margin-top:10px'>{b}</div><div class='sub' style='font-size:25px;margin-top:6px'>{a}</div></div>" for i, b, a in [("🌫", "Düşük görüş", "Sis ve kar kalkış-iniş aralıklarını uzatır"), ("⛓", "Önceki uçuş", "Gecikme bir sonraki seferlere zincirlenir"), ("🛫", "Yoğunluk", "Akşam saatlerinde pist ve kapı trafiği artar"), ("🌧", "Hava durumu", "Rüzgâr ve yağış operasyonu yavaşlatır")])}
 </div>
 <div class='foot'><span>Ayrıntılar blogda</span><span style='color:#5AC8FA'>skytrack ↗</span></div>
</div>""",
}

# ---------- 4 video sahnesi (1080x1920, dikey) ----------
SAHNELER = [
f"""<div class='wrap' style='padding:110px 90px;justify-content:center'>{BRAND}
 <h1 style='margin-top:120px;font-size:120px'>Uçuşun<br><em>yaklaşıyor</em><br>mu?</h1>
 <div style='font-size:260px;margin-top:120px;color:#FFB547;transform:rotate(-12deg)'>✈</div></div>""",
f"""<div class='wrap' style='padding:110px 90px'>{BRAND}
 <h1 style='margin-top:70px;font-size:96px'>Tüm uçuşların<br><em>tek ekranda.</em></h1>
 <div style='margin-top:60px;border-radius:40px;overflow:hidden;border:4px solid #1f3e6b;height:1180px;box-shadow:0 30px 60px rgba(0,0,0,.5)'>
  <img src='{APP_SS}' style='width:100%;display:block'></div></div>""",
f"""<div class='wrap' style='padding:110px 90px'>{BRAND}
 <div style='display:grid;gap:44px;margin-top:150px'>
  {''.join(f"<div class='card' style='display:flex;gap:36px;align-items:center;padding:48px'><span style='font-size:100px'>{i}</span><span style='font-size:62px;font-weight:800;line-height:1.15'>{t}</span></div>" for i, t in [("🗺", "Rotanı<br>haritada gör"), ("⏳", "Geri sayımı<br>takip et"), ("✅", "Hazırlık listeni<br>tamamla")])}
 </div></div>""",
f"""<div class='wrap' style='padding:110px 90px;justify-content:center;align-items:center;text-align:center'>
 <div class='logo' style='width:220px;height:220px;font-size:120px;border-radius:60px'>✈</div>
 <div style='font-size:130px;font-weight:800;margin-top:60px'>SkyTrack</div>
 <div class='sub' style='font-size:56px;margin-top:30px'>Sen yolculuğa odaklan,<br>gerisini SkyTrack hatırlasın.</div>
 <div class='pill' style='margin-top:90px;background:linear-gradient(135deg,#FFB547,#ff9b4a);color:#0B1F3A;font-size:46px;padding:26px 60px'>Ücretsiz dene ↗</div></div>""",
]

def render(html, ad, w, h, hedef):
    f = TMP / f"{ad}.html"; f.write_text(html, encoding="utf-8")
    subprocess.run([sys.executable, EDGE_PY, "png", str(f), str(hedef / f"{ad}.png"), str(w), str(h)], check=True)

for ad, govde in POSTLAR.items():
    render(sayfa(1080, 1080, govde), ad, 1080, 1080, CIKTI)
for i, govde in enumerate(SAHNELER, 1):
    render(sayfa(1080, 1920, govde), f"sahne_{i}", 1080, 1920, SAHNE)
