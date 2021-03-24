from PIL import Image, ImageFilter

img = Image.open('./Image_Folder/astro.jpg')

img.thumbnail((400,400))

img.save('thumbnail.jpg')
