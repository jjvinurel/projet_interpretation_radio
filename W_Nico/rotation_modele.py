from skimage import feature
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from scipy import misc


mod=misc.imread("EpNormCont.jpg")
M=(np.array(mod)[:,:,0])

print("appuyer")
input()
plt.imshow(M)
plt.show()
nx,ny=M.shape
print("nx et ny")
print(nx,ny)
print("appuyer")
input()
