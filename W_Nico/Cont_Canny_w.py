
from skimage import feature
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from scipy import misc
#---------- Read Image ----------#

img = misc.imread("Epaule_normale.jpg")
plt.imshow(img)
plt.show()
print img.shape, img.dtype
print img[100,200,0],img[100,200,1],img[100,200,2],img[100,200,3]
print img.max(),img.min()

M = np.zeros((img.shape[0],img.shape[1]))
print M

M[:,:] = img[:,:,0]

print M.max(),M.min(),M.shape

plt.imshow(M, cmap = plt.get_cmap('gray'))

plt.title("Ep_normale")
plt.savefig("Ep_normale.png")
plt.show()

#---------- Apply Canny  ----------#

edges = feature.canny(M, sigma=1)

fig, ax = plt.subplots()

ax.imshow(edges, cmap=plt.cm.gray, interpolation='nearest')
#ax.axis('off')
ax.set_title('Canny Edge Detection')

plt.savefig("ep_normCanny.png")
plt.imshow(edges)
plt.show()
