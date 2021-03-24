from PIL import Image, ImageFilter

img = Image.open('./Image_Folder/pikachu.jpg')

filtered_Img = img.filter(ImageFilter.BLUR)

filtered_Img.save("blur.png", 'png')

