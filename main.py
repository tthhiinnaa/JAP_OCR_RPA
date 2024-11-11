import PIL.Image
print("Hello")
from manga_ocr import MangaOcr

mocr = MangaOcr()
img = PIL.Image.open()

text = mocr(img)
print(text)