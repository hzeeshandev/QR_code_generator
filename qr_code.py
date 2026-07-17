import qrcode as qr
img = qr.make("https://github.com/hzeeshandev/QR_code_generator")
img.save("Qr_code_generator.png")