# -*- coding: utf-8 -*-
"""Monta o MP4 final: slides ilustrados + narração, cena a cena."""
import os, re, subprocess, shutil
import imageio_ffmpeg

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
FF = imageio_ffmpeg.get_ffmpeg_exe()
SL = os.path.join(HERE, "slides")
AU = os.path.join(ROOT, "audio_vid")
WORK = os.path.join(HERE, "work")
os.makedirs(WORK, exist_ok=True)

CENAS = {1: [1, 2], 2: [3, 4, 5], 3: [6, 7], 4: [8, 9, 10], 5: [11, 12, 13],
         6: [14, 15], 7: [16, 17, 18, 19], 8: [20, 21, 22], 9: [23, 24],
         10: [25, 26, 27]}

def dur(mp3):
    r = subprocess.run([FF, "-i", mp3], capture_output=True, text=True)
    m = re.search(r"Duration: (\d+):(\d+):(\d+\.\d+)", r.stderr)
    h, mi, s = m.groups()
    return int(h) * 3600 + int(mi) * 60 + float(s)

def run(*args):
    r = subprocess.run([FF, "-hide_banner", "-loglevel", "error", *args],
                       capture_output=True, text=True)
    if r.returncode != 0:
        print("ERRO ffmpeg:", r.stderr[:600]); raise SystemExit(1)

segs = []
total = 0.0
for c in range(1, 11):
    mp3 = os.path.join(AU, f"{c:02d}.mp3")
    D = dur(mp3)
    total += D
    ids = CENAS[c]
    per = D / len(ids)
    lst = os.path.join(WORK, f"list{c:02d}.txt")
    with open(lst, "w") as f:
        for i, sid in enumerate(ids):
            f.write(f"file '{os.path.join(SL, f's{sid:02d}.png')}'\n")
            f.write(f"duration {per:.3f}\n")
        f.write(f"file '{os.path.join(SL, f's{ids[-1]:02d}.png')}'\n")
    seg = os.path.join(WORK, f"seg{c:02d}.mp4")
    run("-y", "-f", "concat", "-safe", "0", "-i", lst, "-i", mp3,
        "-vf", "fps=25,format=yuv420p", "-c:v", "libx264", "-preset", "veryfast",
        "-crf", "22", "-c:a", "aac", "-b:a", "160k", "-shortest", seg)
    segs.append(seg)
    print(f"cena {c:02d}: {D:6.1f}s · {len(ids)} slides")

fin = os.path.join(WORK, "final.txt")
with open(fin, "w") as f:
    for s in segs:
        f.write(f"file '{s}'\n")
OUT = os.path.join(ROOT, "output", "Video_Tutorial_PI-I_Loja_Tech.mp4")
run("-y", "-f", "concat", "-safe", "0", "-i", fin, "-c", "copy",
    "-movflags", "+faststart", OUT)
print(f"TOTAL: {total/60:.1f} min -> {OUT} ({os.path.getsize(OUT)//1024//1024} MB)")
