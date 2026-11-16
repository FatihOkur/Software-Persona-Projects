"""
Google Gemini ile üretilen metinsiz görsellerin üzerine marka başlıklarını ve logoyu ekler.
Görüntü modelleri Türkçe metni bozabildiği için metin katmanı HTML/CSS ile ayrıca bindirilir.
Ayrıca video için 1. sahneyi (1080x1920) Gemini görseliyle yeniden üretir.
Kullanım: python gorsel_bindir.py <edge.py yolu>
"""
import pathlib, subprocess, sys

EDGE_PY = sys.argv[1]
KOK = pathlib.Path(__file__).resolve().parent
MEDYA = KOK.parent / "sunum" / "medya"
HAM = MEDYA / "gemini_ham"
TMP = KOK / "_html"; TMP.mkdir(exist_ok=True)
SAHNE = KOK / "_sahneler"; SAHNE.mkdir(exist_ok=True)

CSS = """
*{box-sizing:border-box;margin:0;padding:0}
body{width:Wpx;height:Hpx;overflow:hidden;font-family:'Segoe UI',sans-serif;color:#E8F0FB;background:#0B1F3A}
.bg{position:absolute;inset:0;background-size:cover;background-position:center}
.shade{position:absolute;inset:0}
.wrap{position:absolute;inset:0;padding:72px;display:flex;flex-direction:column}
.brand{display:flex;align-items:center;gap:16px;font-weight:800;font-size:34px;text-shadow:0 2px 12px rgba(0,0,0,.5)}
.logo{width:60px;height:60px;border-radius:18px;display:grid;place-items:center;font-size:32px;color:#0B1F3A;
 background:linear-gradient(135deg,#FFB547,#ff7a45);transform:rotate(-8deg)}
.kick{color:#FFB547;font-weight:700;letter-spacing:.18em;text-transform:uppercase;font-size:24px}
h1{font-size:76px;line-height:1.04;font-weight:800;text-shadow:0 3px 18px rgba(0,0,0,.45)}
h1 em{font-style:normal;color:#FFB547}
.sub{font-size:30px;color:#D4E2F5;text-shadow:0 2px 10px rgba(0,0,0,.6)}
.foot{margin-top:auto;display:flex;justify-content:space-between;align-items:center;font-size:25px;color:#D4E2F5;text-shadow:0 2px 10px rgba(0,0,0,.7)}
.pill{display:inline-block;padding:10px 22px;border-radius:99px;font-weight:700;font-size:26px;background:rgba(11,31,58,.82);border:2px solid #FFB547;color:#FFB547}
.ai{position:absolute;right:20px;bottom:14px;font-size:15px;color:rgba(232,240,251,.55)}
"""
BRAND = "<div class='brand'><div class='logo'>✈</div>SkyTrack</div>"
UST = "linear-gradient(180deg,rgba(7,17,31,.82) 0%,rgba(7,17,31,.35) 38%,rgba(7,17,31,0) 55%,rgba(7,17,31,.55) 100%)"

GORSELLER = {
    "gorsel_1_geri_sayim": ("gemini_1_rota.jpg", f"""
      <div class='wrap'>{BRAND}
        <div class='kick' style='margin-top:56px'>Sıradaki uçuşun</div>
        <h1 style='margin-top:14px'>Kaç gün kaldığını<br><em>bil.</em></h1>
        <div class='foot'><span class='pill'>IST → AMS · 4 gün kaldı</span><span style='color:#5AC8FA'>skytrack ↗</span></div>
      </div>"""),
    "gorsel_2_kontrol_listesi": ("gemini_2_bavul.jpg", f"""
      <div class='wrap'>{BRAND}
        <div class='kick' style='margin-top:40px'>Akıllı yolcu rehberi</div>
        <h1 style='margin-top:10px;font-size:64px'>Havalimanına çıkmadan<br>önce <em>5 kontrol</em></h1>
        <div class='foot'><span>Check-in · kimlik · biniş kartı · bagaj · ulaşım</span><span style='color:#5AC8FA'>↗</span></div>
      </div>"""),
    "gorsel_3_rotar_nedenleri": ("gemini_3_pist.jpg", f"""
      <div class='wrap'>{BRAND}
        <div class='kick' style='margin-top:48px'>Kokpitten bilgi</div>
        <h1 style='margin-top:12px'>Rötar neden olur?</h1>
        <p class='sub' style='margin-top:16px'>🌫 Düşük görüş · ⛓ Önceki uçuş<br>🛫 Yoğunluk · 🌧 Hava durumu</p>
        <div class='foot'><span>Ayrıntılar blogda</span><span style='color:#5AC8FA'>skytrack ↗</span></div>
      </div>"""),
}


def sayfa(w, h, arka, govde, shade=UST):
    css = CSS.replace("Wpx", f"{w}px").replace("Hpx", f"{h}px")
    return (f"<!doctype html><html lang='tr'><head><meta charset='utf-8'><style>{css}</style></head><body>"
            f"<div class='bg' style=\"background-image:url('{arka.as_uri()}')\"></div>"
            f"<div class='shade' style='background:{shade}'></div>{govde}"
            f"<div class='ai'>Görsel: Google Gemini ile üretildi</div></body></html>")


def render(html, ad, w, h, hedef):
    f = TMP / f"{ad}.html"; f.write_text(html, encoding="utf-8")
    subprocess.run([sys.executable, EDGE_PY, "png", str(f), str(hedef / f"{ad}.png"), str(w), str(h)], check=True)


for ad, (ham, govde) in GORSELLER.items():
    render(sayfa(1080, 1080, HAM / ham, govde), ad, 1080, 1080, MEDYA)

# Video 1. sahne: Gemini rota görseli üzerine kanca cümlesi (dikey 1080x1920)
sahne1 = f"""<div class='wrap' style='padding:110px 90px'>{BRAND}
  <h1 style='margin-top:110px;font-size:124px'>Uçuşun<br><em>yaklaşıyor</em><br>mu?</h1></div>"""
render(sayfa(1080, 1920, HAM / "gemini_1_rota.jpg", sahne1,
             "linear-gradient(180deg,rgba(7,17,31,.75) 0%,rgba(7,17,31,.2) 45%,rgba(7,17,31,.35) 100%)"),
       "sahne_1", 1080, 1920, SAHNE)
