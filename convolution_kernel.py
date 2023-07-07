#!/usr/bin/env python3
# coding: UTF-8

import cv2
import numpy as np

image = cv2.imread('test.jpg')
"""
Apply identity kernel
"""
kernel1 = np.array([[0, 0, 0],
                    [0, 1, 0],
                    [0, 0, 0]])
# filter2D() function can be used to apply kernel to an image.
# Where ddepth is the desired depth of final image. ddepth is -1 if...
# ... depth is same as original or source image.
identity = cv2.filter2D(src=image, ddepth=-1, kernel=kernel1)
 
# We should get the same image
cv2.imshow('Original', image)
cv2.imshow('Identity', identity)
 
cv2.waitKey()
cv2.imwrite('identity.jpg', identity)

"""
Apply blurring kernel
"""
kernel2 = np.ones((5, 5), np.float32) / 25
img = cv2.filter2D(src=image, ddepth=-1, kernel=kernel2)
 
cv2.imshow('Original', image)
cv2.imshow('Kernel Blur', img)
 
cv2.waitKey()
cv2.imwrite('blur_kernel.jpg', img)

"""
Apply blurring kernel using blur()
"""
img_blur = cv2.blur(src=image, ksize=(5,5)) # Using the blur function to blur an image where ksize is the kernel size
 
# Display using cv2.imshow()
cv2.imshow('Original', image)
cv2.imshow('Blurred', img_blur)
 
cv2.waitKey()
cv2.imwrite('blur.jpg', img_blur)
cv2.destroyAllWindows()

"""
Apply Gaussian blur
"""
# sigmaX is Gaussian Kernel standard deviation 
# ksize is kernel size
gaussian_blur = cv2.GaussianBlur(src=image, ksize=(5,5), sigmaX=0, sigmaY=0)
 
cv2.imshow('Original', image)
cv2.imshow('Gaussian Blurred', gaussian_blur)
     
cv2.waitKey()
cv2.imwrite('gaussian_blur.jpg', gaussian_blur)

"""
Apply Median blur
"""
# medianBlur() is used to apply Median blur to image
# ksize is the kernel size
median = cv2.medianBlur(src=image, ksize=5)
 
cv2.imshow('Original', image)
cv2.imshow('Median Blurred', median)
     
cv2.waitKey()
cv2.imwrite('median_blur.jpg', median)
cv2.destroyAllWindows()
