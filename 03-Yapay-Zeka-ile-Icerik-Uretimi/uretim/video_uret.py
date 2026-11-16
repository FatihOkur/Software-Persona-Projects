"""4 sahne görselini geçişlerle birleştirip TTS seslendirmesiyle 1080x1920 MP4 tanıtım videosu üretir."""
import pathlib, subprocess
import imageio_ffmpeg

KOK = pathlib.Path(__file__).resolve().parent
MEDYA = KOK.parent / "sunum" / "medya"
SURE = [3.5, 4.5, 5.5, 6.5]          # sahne süreleri (sn), seslendirme cümleleriyle hizalı
GECIS = 0.5                           # geçiş (crossfade) süresi
FFMPEG = imageio_ffmpeg.get_ffmpeg_exe()

girdi = []
for i, s in enumerate(SURE, 1):
    girdi += ["-loop", "1", "-framerate", "30", "-t", str(s), "-i", str(KOK / "_sahneler" / f"sahne_{i}.png")]
girdi += ["-i", str(MEDYA / "skytrack_seslendirme.mp3")]

# Her sahneye hafif yakınlaşma (Ken Burns) + sahneler arasında yumuşak geçiş
filtre = []
for i, s in enumerate(SURE):
    kare = int(s * 30)
    filtre.append(f"[{i}:v]scale=1188:2112,zoompan=z='min(zoom+0.0009,1.08)':x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)'"
                  f":d={kare}:s=1080x1920:fps=30,setsar=1,format=yuv420p[v{i}]")
onceki, ofset = "v0", 0.0
for i in range(1, len(SURE)):
    ofset += SURE[i - 1] - GECIS
    cikis = f"x{i}"
    filtre.append(f"[{onceki}][v{i}]xfade=transition=fade:duration={GECIS}:offset={ofset:.2f}[{cikis}]")
    onceki = cikis
toplam = sum(SURE) - GECIS * (len(SURE) - 1)
filtre.append(f"[{len(SURE)}:a]adelay=300|300,apad,afade=t=out:st={toplam-0.8:.2f}:d=0.8[a]")

komut = [FFMPEG, "-y", *girdi, "-filter_complex", ";".join(filtre), "-map", f"[{onceki}]", "-map", "[a]",
         "-t", f"{toplam:.2f}", "-c:v", "libx264", "-preset", "medium", "-crf", "23", "-pix_fmt", "yuv420p",
         "-c:a", "aac", "-b:a", "128k", "-movflags", "+faststart", str(MEDYA / "skytrack_tanitim_videosu.mp4")]
subprocess.run(komut, check=True, capture_output=True)
print("Video süresi:", toplam, "sn →", MEDYA / "skytrack_tanitim_videosu.mp4")
