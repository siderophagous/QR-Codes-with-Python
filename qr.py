#Import Library
import qrcode
#Generate QR Code
img=qrcode.make('Hello World')
img.save('hello.png')
