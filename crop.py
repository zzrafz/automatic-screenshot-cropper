##
# This program automatically crops Instagram .png prints,
# by removing the white spaces and other stuff above
# and below the image.

import glob
import os
from PIL import Image
list_of_files = glob.glob('./*.png')           # create the list of file
for file_name in list_of_files:
    im = Image.open(file_name)
    width, height = im.size
    centerLine = height // 2
    white = (255, 255, 255)
    for y in range(centerLine, 0, -1) :
        if len([1 for x in range(width) if im.getpixel((x, y)) == white]) == width:
            box = (0, y, width, height)
            crop = im.crop((box))
            crop.save(file_name + "2.png")
            break
    image_file = (file_name + "2.png")
    im = Image.open(image_file)
    width, height = im.size
    white = (255, 255, 255)
    for y in range(1, height, 1) :
        if len([1 for x in range(width) if im.getpixel((x, y)) == white]) == width:
            box = (0, 0, width, y)
            crop = im.crop((box))
            crop.save(file_name + "(2)" + ".png")
            break
    os.remove(file_name + "2.png")