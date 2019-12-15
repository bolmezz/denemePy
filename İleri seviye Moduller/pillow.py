from PIL import Image

image = Image.open("kus.jpg")

degistir = (300,300)

image.thumbnail(degistir)
image.save("kus2.jpg")