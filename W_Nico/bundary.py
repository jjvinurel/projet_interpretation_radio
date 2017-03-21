from skimage.future import graph
from skimage import data, segmentation, color, filters, io
from matplotlib import pyplot as plt
import os
import skimage
from skimage import feature
from scipy import misc
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.image as mpimg



import numpy as np
import matplotlib.pyplot as plt
from skimage.segmentation import random_walker
import skimage


fichier = "D:\W_Nico\Epaule_normale.jpg"
img = misc.imread(fichier)


# Generate noisy synthetic data
data = skimage.img_as_float(img(length=128, seed=1))
data += 0.35 * np.random.randn(*data.shape)
markers = np.zeros(data.shape, dtype=np.uint)
markers[data < -0.3] = 1
markers[data > 1.3] = 2

# Run random walker algorithm
labels = random_walker(data, markers, beta=10, mode='bf')

# Plot results
fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(8, 3.2),
                                    sharex=True, sharey=True)
ax1.imshow(data, cmap='gray', interpolation='nearest')
ax1.axis('off')
ax1.set_adjustable('box-forced')
ax1.set_title('Noisy data')
ax2.imshow(markers, cmap='hot', interpolation='nearest')
ax2.axis('off')
ax2.set_adjustable('box-forced')
ax2.set_title('Markers')
ax3.imshow(labels, cmap='gray', interpolation='nearest')
ax3.axis('off')
ax3.set_adjustable('box-forced')
ax3.set_title('Segmentation')

fig.tight_layout()
plt.show()