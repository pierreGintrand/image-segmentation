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
filename = 'pictures/rouge.png'

#Load the image in RGB space
img = cv2.imread(filename, cv2.IMREAD_COLOR)
img = img.astype(np.int32)

#convert to L*a*b* space
img = cv2.cvtColor(img, cv2.COLOR_RGB2Lab)



