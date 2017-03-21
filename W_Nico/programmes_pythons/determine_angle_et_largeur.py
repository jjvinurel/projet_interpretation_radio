from skimage import feature
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from scipy import misc



#fonction retournant une liste [angle, humerus] 
def largeur_humerus(fichier):

	liste = []

	img = misc.imread(fichier)
	M=(np.array(img)[:,:,0])
	print("dim de im départ",M.shape)
	#print("appuyer")
	#input()
	#plt.imshow(M)
	#plt.show()
	#print("appuyer")
	#input()
	T_rad=M
	#print("appuyer")
	#input()
	#plt.imshow(T_rad)
	#plt.show()
	nx,ny=T_rad.shape
	print("nx et ny")
	print(nx,ny)
	print("appuyer")
	input()
	T_qbd=T_rad[nx//2:,:ny//2]

	#plt.imshow(T_qbd)
	#plt.show()
	#print("appuyer")
	#input()
	M = feature.canny(T_qbd, sigma=2)
	nx,ny=M.shape
	print("nx et ny")
	print(nx,ny)

	#plt.imshow(M, cmap = plt.get_cmap('gray'))
	#plt.show()
	#print("appuyer pour continuer")
	#input()
	#plt.imshow(M)
	#plt.show()
	list_max=np.argmax(M,axis=1)
	#positions des points du bord gauche 
	print(list_max)
	print("appuyer pour continuer")
	input()
	print(np.max(M,axis=1))
	print("appuyer pour continuer fin")
	input()

	prem_seg=np.zeros((nx,ny))
	print("long de list_max",list_max.shape)
	input()
	lim=len(list_max)-1
	for j in range (lim):
	    k=list_max[j]
	    prem_seg [j,k]=255
	plt.imshow(prem_seg)
	plt.show()
	dx=list_max[nx-10]-list_max[nx-50]
	print("dx=",dx)
	#angle d'inclinaison de l'umérus par rapport à la verticale
	angle=np.arctan(dx/40)*180/3.14
	print("angle en dgré=",angle)
	print("prem_seg appuyer pour continuer")
	input()

	#symétrisation de Canny
	T_sym=np.zeros((nx,ny))
	for i in range(ny-1):

	  for j in range(nx-1):

	    pixel= M[j,i]

	    T_sym[j,ny-i-1]= pixel

	plt.imshow(T_sym)
	plt.show()
	print("T_sym appuyer pour continuer fin")
	input()

	list_max_s=np.argmax(T_sym,axis=1)
	print(list_max_s)
	print("appuyer pour continuer")
	input()
	print(np.max(T_sym,axis=1))
	print("appuyer pour continuer fin")
	input()
	#détermination du bord droit de l'umérus
	deux_seg=np.zeros((nx,ny))
	print("long de list_max",list_max_s.shape)
	input()
	lim=len(list_max_s)-1
	for j in range (lim):
	    k=list_max_s[j]
	    deux_seg [j,ny-k-1]=255

	plt.imshow(deux_seg, cmap = plt.get_cmap('gray'))
	plt.show()
	print("appuyer pour continuer")
	input()
	print("points pour écart=",ny-list_max_s[nx-20]-1)
	print("et", list_max[nx-20])
	print("appuyer pour continuer")
	input()
	larg_umerus=np.cos(angle)*(ny-list_max_s[nx-20]-1-list_max[nx-20])
	print("largeur umerus=",larg_umerus,"appuyer pour continuer")
	input()
	
	liste.append(angle)
	liste.append(larg_umerus)

	return liste


fichier = "epD1.jpg"
largeur_humerus(fichier)
