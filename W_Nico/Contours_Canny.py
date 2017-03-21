>>> from skimage import feature
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

#---------- Read Image ----------#

img = mpimg.imread('epD1')

print type(img)
print img.shape, img.dtype
print img[100,200,0],img[100,200,1],img[100,200,2],img[100,200,3]
print img.max(),img.min()

M = np.zeros((img.shape[0],img.shape[1]))
print M

M[:,:] = img[:,:,0]

print M.max(),M.min(),M.shape

plt.imshow(M, cmap = plt.get_cmap('gray'))

plt.title("epD1.jpg")
plt.savefig("epD1")
#plt.show()

#---------- Apply Canny  ----------#

edges = feature.canny(M, sigma=1)
print("dim contour",edges.shape)
print("appuyer")
input()

fig, ax = plt.subplots()

ax.imshow(edges, cmap=plt.cm.gray, interpolation='nearest')
#ax.axis('off')
ax.set_title('Canny Edge Detection')

plt.savefig("LenaCanny.png")
#plt.show()
