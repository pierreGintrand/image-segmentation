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



img = cv2.cvtColor(img, cv2.COLOR_Lab2RGB)




plt.figure()
plt.imshow(img)
plt.xticks([]), plt.yticks([]) # to hide tick values on X and Y axis
plt.show()
