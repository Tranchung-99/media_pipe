#!/usr/bin/env python3
# coding: UTF-8

import cv2
import numpy as np

#python
bright_cube = cv2.imread('bright-cubes.png')
dark_cube = cv2.imread('dark-cubes.png')


#LAB Color space
brightLAB = cv2.cvtColor(bright_cube, cv2.COLOR_BGR2LAB)
darkLAB = cv2.cvtColor(dark_cube, cv2.COLOR_BGR2LAB)

#ycrcb color space 
brightYCB = cv2.cvtColor(bright_cube, cv2.COLOR_BGR2YCrCb)
darkYCB = cv2.cvtColor(dark_cube, cv2.COLOR_BGR2YCrCb)

#HSV color space
brightHSV = cv2.cvtColor(bright_cube, cv2.COLOR_BGR2HSV)
darkHSV = cv2.cvtColor(dark_cube, cv2.COLOR_BGR2HSV)

bgr = [40, 158, 16]
thresh = 40
 
minBGR = np.array([bgr[0] - thresh, bgr[1] - thresh, bgr[2] - thresh])
maxBGR = np.array([bgr[0] + thresh, bgr[1] + thresh, bgr[2] + thresh])

# creates a binary mask where the pixels within a specified range are set 
maskBGR = cv2.inRange(bright_cube,minBGR,maxBGR)
#performs a bitwise AND operation on two input arrays
resultBGR = cv2.bitwise_and(bright_cube, bright_cube, mask = maskBGR)
 
#convert 1D array to 3D, then convert it to HSV and take the first element
# this will be same as shown in the above figure [65, 229, 158]
hsv = cv2.cvtColor( np.uint8([[bgr]] ), cv2.COLOR_BGR2HSV)[0][0]
 
minHSV = np.array([hsv[0] - thresh, hsv[1] - thresh, hsv[2] - thresh])
maxHSV = np.array([hsv[0] + thresh, hsv[1] + thresh, hsv[2] + thresh])

# creates a binary mask where the pixels within a specified range are set 
maskHSV = cv2.inRange(brightHSV, minHSV, maxHSV)
#performs a bitwise AND operation on two input arrays
resultHSV = cv2.bitwise_and(brightHSV, brightHSV, mask = maskHSV)
 
#convert 1D array to 3D, then convert it to YCrCb and take the first element
ycb = cv2.cvtColor( np.uint8([[bgr]] ), cv2.COLOR_BGR2YCrCb)[0][0]
 
minYCB = np.array([ycb[0] - thresh, ycb[1] - thresh, ycb[2] - thresh])
maxYCB = np.array([ycb[0] + thresh, ycb[1] + thresh, ycb[2] + thresh])
 
maskYCB = cv2.inRange(brightYCB, minYCB, maxYCB)
resultYCB = cv2.bitwise_and(brightYCB, brightYCB, mask = maskYCB)
 
#convert 1D array to 3D, then convert it to LAB and take the first element
lab = cv2.cvtColor( np.uint8([[bgr]] ), cv2.COLOR_BGR2LAB)[0][0]
 
minLAB = np.array([lab[0] - thresh, lab[1] - thresh, lab[2] - thresh])
maxLAB = np.array([lab[0] + thresh, lab[1] + thresh, lab[2] + thresh])
 
maskLAB = cv2.inRange(brightLAB, minLAB, maxLAB)
resultLAB = cv2.bitwise_and(brightLAB, brightLAB, mask = maskLAB)
 
cv2.imshow("Result BGR", resultBGR)
cv2.imshow("Result HSV", resultHSV)
cv2.imshow("Result YCB", resultYCB)
cv2.imshow("Output LAB", resultLAB)
cv2.waitKey(0)


