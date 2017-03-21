# -*- coding:utf-8 -*-

import os
import skimage
from skimage import feature
from scipy import misc
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.image as mpimg


def appliquer_canny(fichier, sigma, enregistrer):

	path1 = "D:\W_Nico\images/"
	path = "D:\W_Nico\images\images_cannysees/"

	J = misc.imread(path1 + fichier + '.jpg')
	J = np.array(J)[:,:,0]
	edges = feature.canny(J, sigma=sigma)
	fig, ax = plt.subplots()
	ax.imshow(edges, cmap=plt.cm.gray, interpolation='nearest')
	ax.set_title('Canny Edge Detection')
	if enregistrer == 1:
		plt.savefig(path + fichier + "cannise" + str(sigma) + '.jpg')
	plt.imshow(edges, cmap = plt.get_cmap('gray'))
	plt.show()


#fichier = ""
#appliquer_canny(fichier)
