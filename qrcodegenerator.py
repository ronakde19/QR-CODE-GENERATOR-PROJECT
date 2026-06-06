import qrcode

data = input("Enter the text or url : ").strip()
filename = input("Enter the name of your file: ").strip()

qr = qrcode.QRCode(box_size=10, border=4)
qr.add_data(data)
image = qr.make_image(fill_color='black', back_color='white')
image.save(filename)
print(f'The QR Code saved as {filename}')

