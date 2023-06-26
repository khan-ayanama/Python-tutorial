# installing of pillow library
# change the image extension
# resize image files
# resize multiple images using for loop
# sharpness
# Brightness
# Color
# Contrast
# image blur, Gaussion Blur

from PIL import ImageFilter
from PIL import Image, ImageEnhance
import os

# 1.Change image extension
img1 = Image.open('image1.jpg')
# img1.save('image1.png')

# 2.Show an image in default app
# img1.show()

# 3.Resize image
# MAX_SIZE = (250, 250)
# img1.thumbnail(MAX_SIZE)
# img1.save('dog1small.jpg')

# 4.Working on multiple file

# changing all files jpg to png

# for item in os.listdir():
#     if item.endswith('.jpg'):
#         img1 = Image.open(item)
#         filename, extension = os.path.splitext(item)
#         img1.save(f'{filename}.png')

# 5.Sharpness of image
# import an image inhance module

# img1 = Image.open('image1.jpg')
# enhancer = ImageEnhance.Sharpness(img1)
# enhancer.enhance(0).save('dog1edited.jpg')

# ---------color---------------

# img1 = Image.open('image1.jpg')
# enhancer = ImageEnhance.Color(img1)
# enhancer.enhance(0).save('dog1edited.jpg')

# ------------brightness-----------

# img1 = Image.open('image1.jpg')
# enhancer = ImageEnhance.Brightness(img1)
# enhancer.enhance(2).save('dog1edited.jpg')

# ---------contrast--------

# img1 = Image.open('image1.jpg')
# enhancer = ImageEnhance.Contrast(img1)
# enhancer.enhance(2).save('dog1edited.jpg')

# --------blur--------

img1.filter(ImageFilter.GaussianBlur(radius=1)).save('dogblur.jpg')
