
import skimage
from skimage import feature
from scipy import misc
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.image as mpimg
import os
from canny import *


def seuiller(fichier, seuil):

	path1 = "D:\W_Nico\images/"
	path = "D:\W_Nico\images\images_seuillees/"

	J = misc.imread(path1 + fichier + '.jpg')
	plt.imshow(J, cmap = plt.get_cmap('gray'))
	#plt.savefig(path + fichier + "seuillee" + str(seuil) + '.jpg')
	plt.show()
	J = np.array(J)[:,:,0]
	cannyse = feature.canny(J, sigma=3)
	nx, ny = J.shape
	for i in range (nx-1):
		for j in range (ny-1):
			J[i,j]= J[i,j]<seuil 
			J[i,j]= J[i,j]* 255

	

	plt.imshow(J, cmap = plt.get_cmap('gray'))
	#plt.savefig(path + fichier + "seuillee" + str(seuil) + '.jpg')
	plt.show()
	
	plt.imshow(cannyse, cmap = plt.get_cmap('gray'))
	plt.show()
	


fichier = "Epaule_normale4" 
seuiller (fichier, 170)



