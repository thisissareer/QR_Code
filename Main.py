import pyqrcode
import png
from pyqrcode import QRCode

#Main Code
print("Entre your text for QrCode")
s=input(": ")

#Name for the png image

print("Entre image name to save")
n=input(": ")

#Adding .png

d=n+".png"

#Create QR code

url = pyqrcode.create(s)

#Saving the file as PNG

url.show()
url.png(d, scale =6)

