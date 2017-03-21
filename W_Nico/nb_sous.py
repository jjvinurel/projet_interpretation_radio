# -*- coding:utf-8 -*-
from scipy import misc
import matplotlib.pyplot as plt
import numpy as np
#Choix de l'image à travailler

input("donner le nom de l'image radio")

path = "D:\W_Nico\images\"

I = misc.imread(path1 + fichier + '.jpg')

input("appuyer pour continuer")

T_rad=(np.array(I)[:,:,1])/255
plt.imshow(T_rad, cmap = plt.get_cmap('gray'))



max_x,max_y= T_rad.shape
print(max_x,max_y)
print("max_x et max_y appuyer pour continuer")
input()
nx,ny=T_mod.shape
print(nx,ny)
print("appuyer pour continuer")
input()

#for  i in range(nx-1) :
#    for j in range(ny-1):
 #       if T_mod[i,j]>100:
  #         T_mod[i,j]=255
   #     else:
    #       T_mod[i,j]=0
#plt.imshow(T_mod)
#plt.show()

#print("T_mod appuyer pour continuer")
#input()
#plt.imshow(T_rad)
#plt.show()

#print("T_rad appuyer pour continuer")
#input()
D=np.zeros([nx+1,ny+1])
print("somme D=",D.sum())
print("appuyer")
input()
#plt.imshow(D)
#plt.show()
#print("D à 0 appuyer pour continuer")
#input()

max_nb=0
pos_max_x=0
pos_max_y= 0

for sx in range ((max_x-nx)//25):
    for sy in range ((max_y-ny)//25):
        D=np.zeros([nx,ny])
        #print("sx=",25*sx)
        sox,soy=25*sx,25*sy
        D=T_mod-T_rad[sox:sox+nx-1,soy+ny-1]
        #print(D.sum())       
        if D.sum()>max_nb:
            max_nb=D.sum()
            pos_max_x=sox
            pos_max_y=soy
print("nbs=",D.sum(), "pos=",pos_max_x,pos_max_y)
plt.imshow(255*D)
plt.show()
#print("D maxi appuyer pour continuer")
#input()
raw_input("Appuyer sur une touche pour quitter le programme")
