import cv2
import numpy as np

np

# Load an image using OpenCV
image = cv2.imread('C:\\Users\\RONNA\\Pictures\\wallhaven-m9lxe9.jpg')

# Display the image in a window
cv2.imshow('Image Window', image)
cv2.waitKey(0)
cv2.destroyAllWindows()