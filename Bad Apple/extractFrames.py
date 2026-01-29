#this file wasn't actually used for anything related to the final product
#it just prints out each individual frame as a jpg
#was fun though
#(once again almost all copy and pasted from online)

import cv2

capture = cv2.VideoCapture("movie_resized.mp4")

f = 0

while (capture.isOpened()):
    ret, frame = capture.read()
    if ret == False:
        break

    if not f % 12:
        cv2.imwrite('./frames1/frame'+str(f)+'.jpg', frame)
    f += 1