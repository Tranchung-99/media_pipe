#!/usr/bin/env python3
# coding: UTF-8

# import the cv2 library
import cv2

vid_capture = cv2.VideoCapture('Resources/Cars.mp4')

if (vid_capture.isOpened() == False):
  print("Error opening the video file")
else:
  # Get frame rate information
 
  fps = int(vid_capture.get(5))
  print("Frame Rate : ",fps,"frames per second")  
 
  # Get frame count
  frame_count = vid_capture.get(7)
  print("Frame count : ", frame_count)

  while(vid_capture.isOpened()):
  # vCapture.read() methods returns a tuple, first element is a bool 
  # and the second is frame
    ret, frame = vid_capture.read()
    if ret == True:
        cv2.imshow('Frame',frame)
        k = cv2.waitKey(20)
    # 113 is ASCII code for q key
        if k == 113:
            break
    else:
        break