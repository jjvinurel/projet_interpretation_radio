# -*- coding:utf-8 -*-
import os
from scipy import misc

import matplotlib.pyplot as plt
import numpy as np
from scipy import ndimage
pts = np.array([[10,5],[20,30],[70,20],[50,10]], np.int32)
pts = pts.reshape((-1,1,2))
img = cv2.polylines(img,[pts],True,(0,255,255))
cv2.polylines()
plt.show()
print("appuyer")
input()

