from cv2 import imread
from cv2 import imshow
from cv2 import waitKey
from cv2 import destroyAllWindows
from cv2 import CascadeClassifier
from cv2 import rectangle
pixels = imread('test3.jpg')
classifier = CascadeClassifier('haarcascade_frontalface_default.xml')
bboxes = classifier.detectMultiScale(pixels)
for box in bboxes:
	x, y, width, height = box
	x2, y2 = x + width, y + height
	rectangle(pixels, (x, y), (x2, y2), (0,0,255), 1)
imshow('face detection', pixels)
waitKey(0)
destroyAllWindows()
