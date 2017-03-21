# -*- coding:utf-8 -*-
from scipy import misc

import matplotlib.pyplot as plt
import numpy as np
from scipy import ndimage

J = misc.imread("D:\W_Nico\images/EpNormCont.jpg")
J = np.array(J)[:,:,0]
plt.imshow(J)
plt.show()

K=ndimage.rotate(J,-30.)
plt.imshow(K)
plt.show()
print("appuyer")
input()
