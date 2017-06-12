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

#Load the image in BGR space
img = cv2.imread(filename, cv2.IMREAD_COLOR)

#convert to L*a*b* space
img = cv2.cvtColor(img, cv2.COLOR_BGR2Lab)

#compute the weighted mean

#Gaussian (normal) kernel
def gaussianKernel(x):
    return np.exp(-x/2)

density = np.zeros(img.shape[:2])
width, height = img.shape[:2]
for i in range(width):
    for j in range(height):
        #for each pixel, we calculate the weigthed mean
        #parameters : i, j, img[i,j][0], img[i,j][1], img[i,j][2]
        for p in range(width):
            for q in range(height):
                density[i,j] += gaussianKernel(np.linalg.norm([i,j]-[p,q])**2/(hs**2)) * gaussianKernel(np.linalg.norm([img[i,j][0], img[i,j][1], img[i,j][2]]-[img[p,q][0], img[p,q][1], img[p,q][2]])**2/(hr*2))

img = cv2.cvtColor(img, cv2.COLOR_Lab2RGB)




plt.figure()
plt.imshow(img)
plt.xticks([]), plt.yticks([]) # to hide tick values on X and Y axis
plt.show()
