#!/usr/bin/env python3
# coding: UTF-8


#Contour Relationship represented as matrix: [Next, Previous, First_Child, Parent] 
import cv2

image2 = cv2.imread('input_image2.jpg')
img_gray2 = cv2.cvtColor(image2, cv2.COLOR_BGR2GRAY)
ret, thresh2 = cv2.threshold(img_gray2, 150, 255, cv2.THRESH_BINARY)


#1. retr_list: does not create any parent-child relationship
# contours3, hierarchy3 = cv2.findContours(thresh2, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)
# image_copy4 = image2.copy()
# cv2.drawContours(image_copy4, contours3, -1, (0, 255, 0), 2, cv2.LINE_AA)
# # see the results
# cv2.imshow('LIST', image_copy4)
# print(f"LIST: {hierarchy3}")
# cv2.waitKey(0)
# cv2.imwrite('contours_retr_list.jpg', image_copy4)
# cv2.destroyAllWindows()

#2. retr_external: It only detects the parent contours, and ignores any child contours
# contours4, hierarchy4 = cv2.findContours(thresh2, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
# image_copy5 = image2.copy()
# cv2.drawContours(image_copy5, contours4, -1, (0, 255, 0), 2, cv2.LINE_AA)
# # see the results
# cv2.imshow('EXTERNAL', image_copy5)
# print(f"EXTERNAL: {hierarchy4}")
# cv2.waitKey(0)
# cv2.imwrite('contours_retr_external.jpg', image_copy5)
# cv2.destroyAllWindows()

#3. retr_ccomp: retrieves all the contours in an image. it also applies a 2-level hierarchy to all the shapes or objects in the image
  # All the outer contours will have hierarchy level 1
  # All the inner contours will have hierarchy level 2

# contours5, hierarchy5 = cv2.findContours(thresh2, cv2.RETR_CCOMP, cv2.CHAIN_APPROX_NONE)
# image_copy6 = image2.copy()
# cv2.drawContours(image_copy6, contours5, -1, (0, 255, 0), 2, cv2.LINE_AA)
 
# # see the results
# cv2.imshow('CCOMP', image_copy6)
# print(f"CCOMP: {hierarchy5}")
# cv2.waitKey(0)
# cv2.imwrite('contours_retr_ccomp.jpg', image_copy6)
# cv2.destroyAllWindows()

#4. retr_tree: retrieves all the contours, creates a complete hierarchy
contours6, hierarchy6 = cv2.findContours(thresh2, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
image_copy7 = image2.copy()
cv2.drawContours(image_copy7, contours6, -1, (0, 255, 0), 2, cv2.LINE_AA)
# see the results
cv2.imshow('TREE', image_copy7)
print(f"TREE: {hierarchy6}")
cv2.waitKey(0)
cv2.imwrite('contours_retr_tree.jpg', image_copy7)
cv2.destroyAllWindows()