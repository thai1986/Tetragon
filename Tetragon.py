# import the necessary packages
from __future__ import print_function
from PiVideoStream import *
from ImageProcessing import *
from Quader import *
from picamera.array import PiYUVArray
from picamera import PiCamera
import time
import cv2

DEBUG = False
SIZE = 5
LINE = 239
THRESHOLD = 180
GRAY_CODE_SIZE = 7
QUADER_NUMBER = 20
FRAME_MAX = 200

quaderList = []

for i in range(0, 20):
    quader = Quader(i)
    quaderList.append(quader)

vs = PiVideoStream().start()
vs.camera.vflip = 1
vs.camera.hflip = 1
time.sleep(2.0)
dec = 0
braille = [0, 0, 0]
frameNumber = 0
start = time.time()
try:
    while True:
        frame = vs.read()
        frameNumber+=1
        gray = frame[:,:,0]
        ip = ImageProcessing(gray, SIZE, LINE, THRESHOLD, GRAY_CODE_SIZE)
        if frameNumber > FRAME_MAX:
            end = time.time()
            fps = frameNumber/(end - start)
            print('*****  avg. FPS: {0:0.2f} *****'.format(fps))
            start = time.time()
            frameNumber = 0
        if DEBUG:
            cv2.imshow("Frame", ip.imageDisplay())
            key = cv2.waitKey(1) & 0xFF
        decNew = ip.binaryToDecimal()
        brailleNew = ip.BrailleCode
        if decNew > 79:
            continue
        if decNew % 4 == 0:
            quaderList[decNew // 4].setBraille(brailleNew, 1)
            quaderList[decNew // 4].updateStatus(1)
        if decNew % 4 == 2:
            quaderList[decNew // 4].setBraille(brailleNew, 2)
            quaderList[decNew // 4].updateStatus(2)
        if decNew != dec:
            if quaderList[dec // 4].Status == 3:
                print('Quader[{}] is set'.format(str(dec//4)))
                print('    Braille : {}'.format(str(quaderList[dec // 4].LeftBraille)))
                print('              {}'.format(str(quaderList[dec // 4].RightBraille)))
                quaderList[dec // 4].Status = 4
            dec = decNew
            if DEBUG:
                ip.printInfo()
        if brailleNew != braille:
            braille = brailleNew
            if DEBUG:
                ip.printInfo()
        
        if DEBUG:
            if key == ord("q"):
                break
except KeyboardInterrupt:
    pass
# do a bit of cleanup
cv2.destroyAllWindows()
vs.stop()
