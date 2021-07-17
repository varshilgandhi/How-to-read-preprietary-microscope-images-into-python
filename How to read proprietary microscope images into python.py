# -*- coding: utf-8 -*-
"""
Created on Mon May 10 03:21:50 2021

@author: abc
"""

import czifile

img = czifile.imread('Osteosarcoma_01.czi')
img1 = img[0,0, :, :, 0]

img2 = img1[1, :, :]

import matplotlib.pyplot as plt
plt.imshow(img2, cmap='hot')

 

