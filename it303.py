import cv2
from time import time
from frame import TranslateTAR
TAR = TranslateTAR()

start = time()
#Video capture
cap = cv2.VideoCapture('test1.mp4')

#Extracting frames
i = 0
count = 20
while(cap.isOpened()):

    ret, ogframe = cap.read()

    if not ret:
        break

    if i == 0:
        count = TAR.runOnFrame(ogframe)

    i = (i+1)%count
    k = cv2.waitKey(1) & 0xFF
    if k == 27:
        break

print(TAR.trans.keys())
print(TAR.ext.keys())

print(time() - start)
cap.release()
cv2.destroyAllWindows()