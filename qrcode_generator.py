import qrcode

code = qrcode.make("nsw")
code.save("./images/nsw.png")

code = qrcode.make("vic")
code.save("./images/vic.png")