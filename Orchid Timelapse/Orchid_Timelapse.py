import cv2
from cv2 import waitKey
import numpy as np

import glob

_directory = "C:\\Users\\Steven\\Google Drive\\Orchid Timelapse\\"
_outputfilename = "orchid.avi" #"C:\\Users\\Steven\\Desktop\\orchidvideo.avi"


images = glob.iglob(_directory+"B*.png")

#cv2.namedWindow("Orchid Timelapse")

image_array = []

for im in images:
    orchid = cv2.imread(im)
    image_array += [orchid]
    #cv2.imshow("Orchid Timelapse", orchid)
    #waitKey(100)

num_images = len(image_array)

height, width, layers = image_array[0].shape

video = cv2.VideoWriter(_outputfilename,-1,12,(width,height),isColor=True)
if video.isOpened():
    for i in range(num_images):
        video.write(image_array[i])
else:
    print "error creating video file", _outputfilename


cv2.destroyAllWindows()

video.release()
