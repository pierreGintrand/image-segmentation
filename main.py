# -*- coding: utf-8 -*-
"""
Created on Mon Jun 12 22:19:50 2017

@author: Pierre
"""

# Mean Shift

import cv2
import numpy as np
import matplotlib.pyplot as plt

filename = 'pictures/pills.jpg'
#filename = 'pictures/couleur.png'

#constants
hr = 19
hs = 16
M = 40
look_distance = 4  # How far to look for neighbours.

#Load the image in BGR space
img = cv2.imread(filename, cv2.IMREAD_COLOR)

#convert to L*a*b* space
img = cv2.cvtColor(img, cv2.COLOR_BGR2Lab)

#compute the weighted mean

#Gaussian (normal) kernel
def gaussianKernel(x):
    return np.exp(-x/2)
    
k=0
t=time.time()
density = np.zeros(img.shape[:2])
width, height = img.shape[:2]
for i in range(width):
    print(i)
    for j in range(height):
        #for each pixel, we calculate the weigthed mean
        #parameters : i, j, img[i,j][0], img[i,j][1], img[i,j][2]
        for p in range(max(0, i-look_distance),min(width, i+look_distance)):
            for q in range(max(0, j-look_distance),min(height, j+look_distance)):
                density[i,j] += np.linalg.norm(np.array([i,j])-np.array([p,q]))**2/(hs*2) * gaussianKernel(np.linalg.norm(np.array([img[i,j][0], img[i,j][1], img[i,j][2]])-np.array([img[p,q][0], img[p,q][1], img[p,q][2]])**2/(hr*2)))
img = cv2.cvtColor(img, cv2.COLOR_Lab2RGB)


print(time.time()-t)

plt.figure()
plt.imshow(img)
plt.xticks([]), plt.yticks([]) # to hide tick values on X and Y axis
plt.show()
