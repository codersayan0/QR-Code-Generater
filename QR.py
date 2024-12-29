import qrcode 
from PIL import Image

qr=qrcode.QRCode(version=1,error_correction=qrcode.constants.ERROR_CORRECT_H,box_size=20,border=6,)
qr.add_data("https://codersayan0.github.io/Portfolio/")
qr.make(fit=True)
img=qr.make_image(fill_color="blue",back_color="white")
img.save("Portfolio.png")