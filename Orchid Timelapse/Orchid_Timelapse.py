from __future__ import division

import cv2
from cv2 import waitKey
import numpy as np

import glob


_directory = "C:\\Users\\Steven\\Google Drive\\Orchid Timelapse\\"
_outputfilename = "clahe_orchid.avi" #"C:\\Users\\Steven\\Desktop\\orchidvideo.avi"


images = glob.glob(_directory+"A_*.png")
num_images = len(images)
cv2.namedWindow("Orchid Timelapse")

im1 = images[0]
img1 = cv2.imread(im1)
height, width, layers = img1.shape

video = cv2.VideoWriter(_outputfilename,-1,60,(width,height),isColor=True)

clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))

if video.isOpened():
    n = 0
    for img_path in images:
        img = cv2.imread(img_path)
       
        img2 = np.zeros_like(img)
        for l in range(3):
            img2[:,:,l] = clahe.apply(img[:,:,l])

        cv2.imshow("Orchid Timelapse",img)
        waitKey(1)
        
        video.write(img)
        
        n+=1
        print("%.2f processed."%(100*n/float(num_images)))
else:
    print "error creating video file", _outputfilename
    
#avg_brightness = np.mean(brightness_array, axis=0)
#n=0
#for img_path in images:
#    img = cv2.imread(img_path)
 
#    #hist, bins = np.histogram(img.flatten(),256,[0,256])
    
#    #cdf = hist.cumsum()
#    #cdf_normalized = cdf * hist.max() / cdf.max()

#    #cdf_m = np.ma.masked_equal(cdf,0)
#    #cdf_m = (cdf_m - cdf_m.min())*255/(cdf_m.max()-cdf_m.min())
#    #cdf = np.ma.filled(cdf_m,0).astype('uint8')

#    #img2 = cdf[img]

#    img2 = np.zeros_like(img)
#    for l in range(3):
#        img2[:,:,l] = cv2.equalizeHist(img[:,:,l])

#    cv2.imshow("Orchid Timelapse",img2)
#    waitKey(1)
#    n+=1
cv2.destroyAllWindows()

video.release()
