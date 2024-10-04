import qrcode
qr = qrcode.make("http://localhost:3000/")
qr.save("qr.jpg")