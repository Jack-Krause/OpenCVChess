import cv2
from matplotlib import pyplot as plt
import numpy as np
  
# Opening image
img = cv2.imread("cb1.jpg")
lsd = cv2.createLineSegmentDetector(0)
  
# OpenCV opens images as BRG 
# but we want it as RGB We'll 
# also need a grayscale version
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
  
edges = cv2.Canny(img_gray, 100, 200)
lines = lsd.detect(img_gray)

#plt.subplot(121),plt.imshow(img,cmap = 'gray')
#plt.title('Original Image'), plt.xticks([]), plt.yticks([])
#plt.subplot(122),plt.imshow(edges,cmap = 'gray')
#plt.title('Edge Image'), plt.xticks([]), plt.yticks([])
#plt.show()
#for edge in edges:
#    print(edge)

    
for line in lines:
    round(line, 1)
    
    
drawn_img = lsd.drawSegments(img_rgb, lines[0])
plt.imshow(drawn_img, cmap="gray")
plt.show()