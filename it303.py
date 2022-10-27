import cv2
from frame import TranslateTAR
TAR = TranslateTAR()

#Video capture
cap = cv2.VideoCapture('it303.mp4')

#Extracting frames
while(cap.isOpened()):
    ret, ogframe = cap.read()

    if not ret:
        break
    
    ogframe = cv2.flip(ogframe, 0)
    ogframe = cv2.flip(ogframe, 1)
    TAR.runOnFrame(ogframe)

    k = cv2.waitKey(1) & 0xFF
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()