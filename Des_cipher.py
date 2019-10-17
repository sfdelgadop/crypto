import base64
from pyDes import *
from PIL import Image
import io

with open("hitagi.jpg", "rb") as image:
    file = image.read()
    biteArrayImage = bytearray(file)

k = des(b"DESCRYPT", CBC, b"\0\2\3\4\5\6\7\0", pad=None, padmode=PAD_PKCS5)
desImage = k.encrypt(biteArrayImage)
base = base64.b64encode(desImage)
print(base)
base_ = base64.b64decode(base)
desImage_ = k.decrypt(base_)
image = Image.open(io.BytesIO(desImage_))
image.save("hitagiDecrypt.jpg")
