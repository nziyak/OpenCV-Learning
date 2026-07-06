from numpy import uint8
import numpy as np 
import matplotlib.pyplot as plt
import cv2

img = cv2.imread("images/saat.png")

plt.imshow(img)
plt.show()

fixed_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

plt.imshow(fixed_img)
plt.show()
print(fixed_img.shape)

rszd_img = cv2.resize(fixed_img, (500,300))

plt.imshow(rszd_img)
plt.show()

w_ratio = 0.5
h_ratio = 0.5
rt_img = cv2.resize(fixed_img, (0,0), fixed_img, w_ratio, h_ratio)

plt.imshow(rt_img)
plt.show() 
print(rt_img.shape)

flp_img = cv2.flip(fixed_img, 0)

plt.imshow(flp_img)
plt.show() 

arr = np.ones((900,900), dtype=np.uint8) * 255 #8 bitlik intlerden oluşan, bembeyaz
arr[:, 450:] = arr[:, 450:] * 0.5

cv2.imwrite("images/hmm.jpg", arr)
hmm = cv2.imread("images/hmm.jpg")
plt.imshow(hmm)
plt.show() 
