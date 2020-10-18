import cv2
import numpy as np
import os

img_dir = "pairs"
for i in range(1,int(len(os.listdir(img_dir))/2)+1):
    num = format(i, "02")
    im_l = cv2.imread(img_dir+"/left_"+num+".jpeg")
    im_r = cv2.imread(img_dir+"/right_"+num+".jpeg")

    im_v = cv2.hconcat([im_l, im_r])
    cv2.imwrite('calibration_pictures/pair_'+num+".jpeg", im_v)