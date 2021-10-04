import pyqrcode
from pyqrcode import QRCode
s="hi this is gurkirat"
q=pyqrcode.create(s)
q.svg("myicon.png",scale=8)
