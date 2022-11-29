import numpy as np
import cv2
from PIL import Image

INTRO_SKIP = 60
READ_ROW = 0
BPM = 100
FPS = 30
KEYBOARD_KEYS = 28

VIDEO_PATH = 'IO/video.mp4'

if __name__=="__main__":
    
    cap = cv2.VideoCapture(VIDEO_PATH)
    count = 0
    while cap.isOpened():
        if count>INTRO_SKIP:
            ret,frame = cap.read()
            # print(count,frame[0,0])
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            im_pil = Image.fromarray(frame)
            im_pil = im_pil.convert('L')
            cv2.imshow('window-name', np.asarray(im_pil))
            

        # cv2.imshow('window-name', frame)
        # cv2.imwrite("frame%d.jpg" % count, frame)
        count +=1
        if cv2.waitKey(10) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows() # destroy all opened windows
