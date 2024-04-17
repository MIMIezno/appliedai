import cv2
import numpy as np

cap = cv2.createBackgroundSubtractorKNN()

capture = cv2.VideoCapture(0)

if not capture.isOpened():
    print('ERROR!')
    exit(0)

while True:
    #ret= return
    #frame will display the output
    ret, frame = capture.read()
    if frame is None:
        break

#to resize the frame (w, h)
    frame = cv2.resize(frame, (600,500))

#detecting the moving object in the videos
    foregMask = cap.apply(frame)

#to clean dirt in any specific object
    kernel = np.ones((5,5), np.uint8)

    foregMask   = cv2.erode(foregMask, kernel, iterations=2)
    foregMask   = cv2.dilate(foregMask, kernel, iterations=2)

#for frame numbers on frame
#    cv2.rectangle(frame, (10,2), (100,20), (255,255,255), -1)

#to remove noises
    foregMask[np.abs(foregMask)< 250] = 0

# to display the orig. and the foregmask
    cv2.imshow('Frame', frame)
    cv2.imshow('Forground Mask', foregMask)

    key = cv2.waitKey(33)
    if key == 'p'  or key == 27:
        break


    

    