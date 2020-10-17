# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


import cv2
import numpy as np
import os

# Playing video from file:
#cap = cv2.VideoCapture('/Users/becca085/Desktop/rex_video.MP4')
cap = cv2.VideoCapture(0)
cv2.namedWindow("live_video")

try:
    if not os.path.exists('data'):
        os.makedirs('data')
except OSError:
    print('Error: Creating directory of data')

currentFrame = 0

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    if not ret:
        print("failed to grab frame")
        break
    cv2.imshow("live_video", frame)

    k = cv2.waitKey(1)
    if k % 256 == 27:
        # ESC pressed
        print("Escape hit, closing...")
        break

    # Saves image of the current frame in jpg file
    name = './data/frame' + str(currentFrame) + '.jpg'
    print ('Creating...' + name)
    cv2.imwrite(name, frame)

    # To stop duplicate images
    currentFrame += 1

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
