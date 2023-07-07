#!/usr/bin/env python3
# coding: UTF-8

import numpy as np
import cv2
import mediapipe as mp
import time

cap = cv2.VideoCapture("/dev/video2")

# Check if the webcam is opened correctly
if not cap.isOpened():
    raise IOError("Cannot open webcam")

while True:
    ret, frame = cap.read()
    frame = cv2.resize(frame, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_AREA)
    cv2.imshow('Input', frame)

    BaseOptions = mp.tasks.BaseOptions
    DetectionResult = mp.tasks.components.containers.detections.DetectionResult
    ObjectDetector = mp.tasks.vision.ObjectDetector
    ObjectDetectorOptions = mp.tasks.vision.ObjectDetectorOptions
    VisionRunningMode = mp.tasks.vision.RunningMode

    def print_result(result: DetectionResult, output_image: mp.Image, timestamp_ms: int):
        print('detection result: {}'.format(result))

    options = ObjectDetectorOptions(
        base_options=BaseOptions(model_asset_path='/path/to/model.tflite'),
        running_mode=VisionRunningMode.LIVE_STREAM,
        max_results=5,
        result_callback=print_result)

    with ObjectDetector.create_from_options(options) as detector:
    # The detector is initialized. Use it here.
        # Use OpenCV’s VideoCapture to start capturing from the webcam.

    # Create a loop to read the latest frame from the camera using VideoCapture#read()

    # Convert the frame received from OpenCV to a MediaPipe’s Image object.
        mp_image = mp.Image(image_format = mp.ImageFormat.SRGB, data=frame)

    # Send the latest frame to perform object detection.
    # Results are sent to the `result_callback` provided in the `ObjectDetectorOptions`.
        detection_result = detector.detect_async(mp_image, time.time())


    c = cv2.waitKey(1)
    if c == 27:
        break

cap.release()
#cv2.destroyAllWindows()

