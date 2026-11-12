import base64, pathlib, shutil
out = pathlib.Path("out")
out.mkdir(exist_ok=True)
for f in ["index.html", "download.html"]:
    shutil.copy(f, out / f)
for src, dst in [("assets/logo.b64", "logo.png"), ("assets/icon-192.b64", "icon-192.png"), ("assets/qr.b64", "nexchat-download-qr.png")]:
    (out / dst).write_bytes(base64.b64decode(pathlib.Path(src).read_text()))
with open(out / "app-debug.apk", "wb") as o:
    for p in sorted(pathlib.Path("chunks").glob("part-*.b64")):
        o.write(base64.b64decode(p.read_text()))
print("built", (out / "app-debug.apk").stat().st_size)
