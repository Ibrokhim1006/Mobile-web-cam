import requests
import cv2
import numpy as np
import imutils
import os


url = "http://192.168.1.5:8080/shot.jpg"

while True:
    img_res = requests.get(url)
    img_arr = np.array(bytearray(img_res.content),dtype=np.uint8)
    img = cv2.imdecode(img_arr,-1)
    im = imutils.resize(img,width=1000,height=1800)
    cv2.imshow("Android_cam",img)

    if cv2.waitKey(1)==27:
        break
cv2.destroyAllWindows()



