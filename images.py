from PIL import Image, ImageFilter

img = Image.open('./Image_Folder/pikachu.jpg')

filtered_Img = img.convert('L')

filtered_Img.save("grey.png", 'png')

