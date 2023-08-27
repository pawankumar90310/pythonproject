import qrcode
qr=qrcode.QRCode(
    version=12,
    box_size=13,
    border=15
)

data="https://www.youtube.com/channel/UCKLQ--BjbehU4p7RQZKNslg"
qr.add_data(data)
qr.make(fit=True)
img=qr.make_image(fill="red",back_color="green")
img.save('text.png')