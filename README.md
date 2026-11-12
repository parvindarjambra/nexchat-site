# NexChat download site

Public download page for the NexChat Android app, live at
https://nexchatpk.vercel.app/ — QR code + APK download.

The APK is stored as base64 chunks under `chunks/` (the GitHub connector
cannot push binary files). The Vercel build (`python3 join.py`) reassembles
them into `app-debug.apk` and decodes the logo/QR images from `assets/`.

Deployed via Vercel Git integration on the `nexchat` project.
