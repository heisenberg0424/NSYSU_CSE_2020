from PIL import Image
from PIL import ImageEnhance
import cv2
import numpy as np
import matplotlib.pyplot as plt
img = Image.open('test.jpg')

#256-gray-level
img=img.convert('L')
#gray.show()

#contrast brightness
X=0
br=ImageEnhance.Brightness(img).enhance(X)
br=ImageEnhance.Contrast(img).enhance(X)
#br.show()

#Zoom in and shrink
resize=img.resize((1920,1080),Image.BILINEAR)
#resize.show()

#rotate
rot=img.rotate(90,expand=True)
#rot.show()

#histogram
array=np.asarray(img)
hist=[0]*256
hist=np.array(hist)
for x in range(array.shape[0]):
    for y in range (array.shape[1]):
        i = array[x,y]
        hist[i]=hist[i]+1
plt.plot(hist,color='darkgrey')
plt.axis('off')
plt.savefig('foo.png')

#auto level
cvimg=np.array(img)
eq = cv2.equalizeHist(cvimg)
#cv2.imshow('OpenCV',eq)
#cv2.waitKey(0)
#print(type(resize.width))