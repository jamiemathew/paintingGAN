# resize pokeGAN.py
import os
import cv2
from PIL import Image


src = "./fullimages" #pokeRGB_black
dst = "./resizedData" # resized

os.mkdir(dst)

for each in os.listdir(src):
    img = cv2.imread(os.path.join(src,each))
    img = cv2.resize(img,(64,64))
    cv2.imwrite(os.path.join(dst,each), img)
    

current_dir = os.getcwd()
image_dir = os.path.join(current_dir, dst)
destination_dir = os.path.join(current_dir, 'smallimages')
images = []
i = 0
for filename in os.listdir(image_dir):
  im = Image.open(os.path.join(image_dir, filename))
  name = filename.split('.')
  new_name = str(i) +'.png'
  im.save(os.path.join( destination_dir, new_name))
  i+=1