
from skimage.color import rgb2gray
import numpy as np
import matplotlib.pyplot as plt
import cv2
from PIL import Image

# 灰度话
img = cv2.imread('lenna.png')
h,w = img.shape[:2]
img_gray = np.zeros([h,w],img.dtype)
for i in range(h):
    for j in range(w):
        m = img[i,j]
        img_gray[i,j] = int(m[0]*0.11 + m[1]*0.59 + m[2]*0.3)
print(img_gray)
cv2.imshow("image show gray",img_gray)
cv2.waitKey(0)

#二值化
rows, cols = img_gray.shape
for i in range(rows):
    for j in range(cols):
        if(img_gray[i,j] <=0.5):
            img_gray[i,j] = 0
        else:
            img_gray[i,j] = 1
print(img_gray)
cv2.imshow("image",img_gray)
cv2.waitKey(0)