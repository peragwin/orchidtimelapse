import cv2
from cv2 import waitKey
import numpy as np

import glob

_directory = "C:\\Users\\Steven\\Google Drive\\Orchid Timelapse\\"
_outputfilename = "orchid.avi" #"C:\\Users\\Steven\\Desktop\\orchidvideo.avi"


images = glob.glob(_directory+"A*.png")
num_images = len(images)
#cv2.namedWindow("Orchid Timelapse")

im1 = images[0]
img1 = cv2.imread(im1)
height, width, layers = img1.shape

video = cv2.VideoWriter(_outputfilename,-1,12,(width,height),isColor=True)

if video.isOpened():
    video.write(img1)
    n = 1
    for img_path in images:
        img = cv2.imread(img_path)
        video.write(img)
        print("%.2f processed."%(100*n/float(num_images)))
        n+=1
else:
    print "error creating video file", _outputfilename


cv2.destroyAllWindows()

video.release()
