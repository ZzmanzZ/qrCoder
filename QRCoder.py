import qrcode

#Input
qrdata = input("What would you like to encode? \n")
color = input("What color code do you want? \n")
background = input("What background color do you want? \n")
name = input("What would you like to name your qrcode? \n")
#processing
qr = qrcode.QRCode(version = 1, box_size = 20, border = 10)
qr.add_data(qrdata)
qrimage = qr.make_image(fill_color = color, back_color = background)
#Export
qrimage.save(name + ".png")


