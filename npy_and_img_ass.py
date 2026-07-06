import numpy as np 
import matplotlib.pyplot as plt

from PIL import Image 

# 5,5 boyutunda bi matris oluştur 10 ile dolu olsun 
arr = np.ones((5,5))

arr = arr*10

print(arr)

img = Image.open("images/saat.png")
plt.imshow(img)
plt.show()

imarr = np.asarray(img)

imarrB = imarr.copy()

imarrB[:,:,0] = 0
imarrB[:,:,1] = 0

plt.imshow(imarrB)
plt.show()