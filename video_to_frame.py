import sys
import os

import cv2


def Video2Frames(videofile):
    ''' this function get a video file name like mouse.mp4 as input
    and read all frames of the video . then save all frames in the same directory 
    by the foramt of "videoname_ + number .png " 
    which the number is the number of  the frame.'''

    cap = cv2.VideoCapture(videofile) #"shoe.mp4"
    cnt = 0
    while(True):
        # Capture frame-by-frame
        captured, frame = cap.read()
        if not captured:
            break
        #resize each frame for a better view
        scale_percent = 50 # percent of original size
        width = int(frame.shape[1] * scale_percent / 100)
        height = int(frame.shape[0] * scale_percent / 100)
        dim = (width, height)
        
        # resize image
        resized = cv2.resize(frame, dim, interpolation = cv2.INTER_AREA)
        #just because we know :)
        if videofile == "shoe.mp4":
            if cnt == 35 or cnt == 39 :
                cv2.imwrite("{0}_{1}.png".format(videofile[:videofile.find('.')] ,cnt),resized)
        elif videofile == "mouse.mp4":
            if cnt == 78 or cnt == 81 : 
                cv2.imwrite("{0}_{1}.png".format(videofile[:videofile.find('.')] ,cnt),resized)
        else:
            cv2.imwrite("{0}_{1}.png".format(videofile[:videofile.find('.')] ,cnt),resized)
        cnt += 1
    
    # When everything done, release the capture
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    
    Video2Frames( sys.argv[1])