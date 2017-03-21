# -*- coding:utf-8 -*-
from scipy import misc
import matplotlib.pyplot as plt
import numpy as np

J = misc.imread("FractureSubtile.JPEG")
print (J[10, 20])
print(J.shape)
plt.imshow(J)
plt.show()

