# QR code generator using "qrcode" library

import qrcode

# box and border sizes of QR code

qr = qrcode.QRCode(version=1,
                   error_correction=qrcode.constants.ERROR_CORRECT_L,
                   box_size=20,
                   border=2)

# string we want to be seen by costumer
qr.add_data("в...")
qr.make(fit=True)

# Change colours
img = qr.make_image(fill_color="black", back_color="pink")

# save as image
img.save("ber.png")
