# -*- coding:utf-8 -*-

import os
import skimage
from skimage import feature
from scipy import misc
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.image as mpimg


def appliquer_canny(fichier):


	J = misc.imread(fichier)
	J = np.array(J)[:,:,0]
	edges = feature.canny(J, sigma=0.5)
	fig, ax = plt.subplots()
	ax.imshow(edges, cmap=plt.cm.gray, interpolation='nearest')
	ax.set_title('Canny Edge Detection')

	plt.savefig("{}canny.jpg".format(fichier))
	plt.imshow(edges, cmap = plt.get_cmap('gray'))
	plt.show()


#fichier = ""
#appliquer_canny(fichier)
