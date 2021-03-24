from PIL import Image, ImageFilter

img = Image.open('./Image_Folder/pikachu.jpg')

filtered_Img = img.filter(ImageFilter.BLUR)
#use png format while using filter
filtered_Img.save("blur.png", 'png')

