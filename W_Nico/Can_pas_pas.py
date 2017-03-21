from skimage import feature
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from scipy import misc
#---------- Read Image ----------#

img = misc.imread("D:\W_Nico\images\epD1.jpg")
plt.imshow(img)
plt.show()
print("appuyer pour continuer")
input()
M = np.zeros((img.shape[0],img.shape[1]))
M[:,:] = img[:,:,0]
plt.imshow(M, cmap = plt.get_cmap('gray'))

plt.title("epD1")
plt.savefig("epD1")
plt.show()
edges = feature.canny(M, sigma=2)
print("dim de im canny",edges.shape)
print("appuyer")
input()

fig, ax = plt.subplots()
ax.imshow(edges, cmap=plt.cm.gray, interpolation='nearest')
ax.set_title('Canny Edge Detection')

#plt.savefig("epD1CannyStest.jpg")
plt.imshow(edges)
plt.show()
print (M[6,:])
print("appuyer pour continuer")
input()
#N=255-misc.imread("epD1CannyStest.jpg")
#plt.imshow(N)
#plt.show()
#print (N[6,:])
#print("appuyer pour continuer")
#input()
