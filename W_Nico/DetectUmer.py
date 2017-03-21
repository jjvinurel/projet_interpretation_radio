# -*- coding:utf-8 -*-
import os
import skimage
from skimage import feature
from scipy import misc
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.image as mpimg
J = misc.imread("FractureSubtile.JPEG")
print (J[10, 20])
print(J.shape)
plt.imshow(J)
plt.show()
print("appuyer")
input()
T_rad=(np.array(J)[:,:,0])
plt.imshow(T_rad)
plt.show()
nx,ny=T_rad.shape
print("nx et ny")
print(nx,ny)
dec=8
print("dec=",dec)
print("appuyer")
input()
T_qbd=T_rad[nx//2:,:ny//2]

plt.imshow(T_qbd)
plt.show()
print("appuyer")
input()
edges = feature.canny(T_qbd, sigma=2)
fig, ax = plt.subplots()
ax.imshow(edges, cmap=plt.cm.gray, interpolation='nearest')
ax.set_title('Canny Edge Detection')

plt.savefig("qbdCannyFractureSubtile.jpg")
plt.imshow(edges)
plt.show()
print("appuyer")
input()
print(edges.sum())
print("appuyer")
input()

fichier_depart = "FractureSubtile.JPEG"
fichier_enregistre = "{qbdCannyFractureSubtile.jpg"