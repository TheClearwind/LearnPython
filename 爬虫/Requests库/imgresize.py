import cv2
import os
imgs=os.listdir('result')
for i in imgs:
    image=cv2.imread('result/'+i)
    res=cv2.resize(image,(640,360),interpolation=cv2.INTER_CUBIC)
    cv2.imwrite('resize_result/'+i,res)
print('Done')