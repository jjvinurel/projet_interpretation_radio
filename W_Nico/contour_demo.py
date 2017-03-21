"""
Illustrate simple contour plotting, contours on an image with
a colorbar for the contours, and labelled contours.

See also contour_image.py.
"""
import matplotlib
import numpy as np
import matplotlib.cm as cm
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt

import matplotlib.pyplot as plt
from scipy import interpolate
from scipy.interpolate import interp1d


x = [1, 3, 5, 3]
y = [2, 4, 3, 2]


f = interp1d(x, y)
f2 = interp1d(x, y, kind='cubic')

xnew = x
import matplotlib.pyplot as plt
plt.plot(x, y, 'o', xnew, f(xnew), '-', xnew, f2(xnew), '--')
plt.legend(['data', 'linear', 'cubic'], loc='best')
plt.show()