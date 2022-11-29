import numpy as np
import cv2
from PIL import Image, ImageOps
import math

INTRO_SKIP = 0
READ_ROW = 0
BPM = 100
FPS = 30
KEYBOARD_KEYS = 88

LEFT_INDEX = 0

VIDEO_PATH = 'IO/video.mp4'

if __name__=="__main__":
    
    cap = cv2.VideoCapture(VIDEO_PATH)
    count = 0
    while cap.isOpened():
        if count>INTRO_SKIP:
            ret,frame = cap.read()

            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

            im_pil = Image.fromarray(frame)
            im_pil = ImageOps.invert(im_pil.convert('L'))

            fr = np.asarray(im_pil)
            r1 = fr[0]

            L = len(r1)
            D = math.ceil((L/KEYBOARD_KEYS))

            for i in range(len(fr[0])):
                for j in range(1):
                    # fr[j][i] = round(fr[j][i]/255)*255
                    fr[j][i] = 0 if fr[j][i]<180 else 255
            
            for i in range(KEYBOARD_KEYS-1):
                idx = LEFT_INDEX+round(D/2)+round(i*D)
                for r in range(20,fr.shape[0]):
                    fr[r][idx] = 0
            
            for i in range(KEYBOARD_KEYS-1):
                idx = LEFT_INDEX+round(D/2)+round(i*D)
                if fr[0][idx] == 0:
                    if (fr[0][idx - round(D/3)] == 0) and (fr[0][idx + round(D/3)] == 0):
                        for r in range(500,fr.shape[0]):
                            for k in range(-5,5):
                                fr[r][idx+k] = 0
                
            fr[0] = r1

            # fr = cv2.cvtColor(fr,cv2.COLOR_GRAY2RGB)

            cv2.imshow('window-name', fr)
            
        else:
            ret = cap.read()
        # cv2.imshow('window-name', frame)
        # cv2.imwrite("frame%d.jpg" % count, frame)
        count +=1
        if cv2.waitKey(10) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows() # destroy all opened windows
