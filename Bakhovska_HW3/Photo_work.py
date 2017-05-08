#!/usr/bin/env python 3

import os
import glob
import sys

from PIL import Image, ImageFilter

if (len(sys.argv) < 2):
    print("Missing path to photo folder")
    sys.exit()

photo_list = []
for root, dirs, files in os.walk(sys.argv[1]):
    photo_list += glob.glob(os.path.join(root, '*.jpg'))

for photo_path in photo_list:
    try:
        img = Image.open(photo_path).convert('L') #img.convert('L')
        if img.size[0] < img.size[1]:
            img = img.rotate(90, expand=1)
        img.save(photo_path)
    except OSError as e:
        print("Помилка при відкритті файлу \"{0}\": {1}".format(photo_path, e.strerror))
    except:
        print("Неочікувана помилка \"{0}\"".format(photo_path))



