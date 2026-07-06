import numpy as np 
import matplotlib.pyplot as plt 
from PIL import Image as img

pic = img.open("images/saat.png")

plt.imshow(pic)
plt.show()
print(type(pic))

pic_arr = np.asarray(pic)

print(type(pic_arr))
print(pic_arr.shape)

pic_red = pic_arr.copy()

# R G B A
#red channel values
#in gray scale. siyah yerler kırmızının az olduğu, beyazlar çok olduğu yerler.
#[:,:,0] şu demek: tüm satırları ve tüm sütunları al, sonra da 0 indeksindeki renk kanalını al yani red
plt.imshow(pic_red[:,:,0], cmap="gray")
plt.show()

pic_red[:,:,1] = 0 #yeşil kalanını 0lıyoruz
plt.imshow(pic_red)
plt.show()

pic_red[:,:,2] = 0 #mavi kanalın katkısını da sıfırıadık
plt.imshow(pic_red)
plt.show() 

