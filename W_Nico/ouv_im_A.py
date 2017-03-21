# -*- coding:utf-8 -*-
from scipy import misc
import matplotlib.pyplot as plt
import numpy as np

J = misc.imread("EpNormCont.jpg")
print (J[120, 120])
plt.imshow(J)
plt.show()

