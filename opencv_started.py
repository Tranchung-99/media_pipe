#!/usr/bin/env python3
# coding: UTF-8

# import the cv2 library
import cv2
 
# The function cv2.imread() is used to read an image.
img_grayscale = cv2.imread('test.jpg',0)   # Other: img_grayscale = cv2.imread('test.jpg', cv2.IMREAD_GRAYSCALE)
img_color = cv2.imread('test.jpg', 1)  # Other: img_color = cv2.imread('test.jpg', IMREAD_COLOR)
img_unchanged = cv2.imread('test.jpg',-1)  # Other: img_unchange = cv2.imread('test.jpg', cv2.IMREAD_UNCHANGED)
# The function cv2.imshow() is used to display an image in a window.
cv2.imshow('graycsale image',img_grayscale)
 
# waitKey() waits for a key press to close the window and 0 specifies indefinite loop
cv2.waitKey(0)
 
# cv2.destroyAllWindows() simply destroys all the windows we created.
cv2.destroyAllWindows()
 
# The function cv2.imwrite() is used to write an image.
cv2.imwrite('grayscale.jpg',img_grayscale)