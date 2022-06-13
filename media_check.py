import os

path = r'C:\Users\path\path'
txt = 0
srt = 0
png = 0
jpg = 0
mp4 = 0
mkv = 0

for root, dirs, file in os.walk(path):
    for item in file:
        if ".txt" in item:
            txt = txt + 1
            print("[TXT]", root, item)
        if ".srt" in item:
            srt = srt + 1
            print("[SRT]", root, item)
        if ".mp4" in item:
            mp4 = mp4 + 1
            print("[MP4]", root, item)
        if ".mkv" in item:
            mkv = mkv + 1
            print("[MKV]", root, item)
        if ".png" in item:
            png = png + 1
            print("[PNG]", root, item)
        if ".jpg" in item:
            jpg = jpg + 1
            print("[JPG]", root, item)

total = txt + srt + png + jpg + mp4 + mkv
print("{} files analyzed".format(total))
print("{} TXT".format(txt))
print("{} SRT".format(srt))
print("{} PNG".format(png))
print("{} JPG".format(jpg))
print("{} MP4".format(mp4))
print("{} MKV".format(mkv))