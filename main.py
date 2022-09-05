from PIL import Image
import os
import numpy as np
import cv2

def changedH(bgr_img, shift):
    hsvimage = cv2.cvtColor(bgr_img, cv2.COLOR_BGR2HSV_FULL)
    hi = hsvimage[:,:,0].astype(np.int32)
    if shift < 0:
        nhi = hi.flatten()
        for px in nhi:
            if px < 0:
                px = 255 - px
        nhi = nhi.reshape(hsvimage.shape[:2])
        hi = nhi.astype(np.uint8)
    chimg = (hi + shift) % 255
    hsvimage[:,:,0] = chimg
    hsv8 = hsvimage.astype(np.uint8)
    return cv2.cvtColor(hsv8,cv2.COLOR_HSV2BGR_FULL)

bgr_img = cv2.imread('image.png', cv2.IMREAD_COLOR)

a = []

for i in range(1,21):
    a.append(changedH(bgr_img, i*30))

num = 0
for item in a:
    cv2.imwrite(str(num)+'.png',item)
    num += 1
cv2.waitKey(0)

pictures=[]

for i in range(1,20):
    pic_name=str(i)+ '.png'
    img = Image.open(pic_name)
    pictures.append(img)

pictures[0].save('gaming.gif',save_all=True, append_images=pictures[1:],
optimize=False, duration=50, loop=0)

for i in range(0,20):
    os.remove(str(i)+".png")
