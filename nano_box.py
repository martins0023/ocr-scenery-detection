import cv2
import pytesseract
img = cv2.imread('das.png')
h, w, c = img.shape
boxes = pytesseract.image_to_boxes(img)
for b in boxes.splitlines():
    b = b.split(' ')
    img = cv2.rectangle(img, (int(b[1]), h - int(b[2])), (int(b[3]), h - int(b[4])), (0, 255, 0), 2)
cv2.imshow('img', img)
cv2.waitKey(0)

import cv2
import pytesseract
from pytesseract import Output
img = cv2.imread('new.png')
d = pytesseract.image_to_data(img, output_type=Output.DICT)
print(d.keys())

output = open('moral.txt', 'w')


n_boxes = len(d['text'])
output.write(n_boxes)
for i in range(n_boxes):
    if int(d['conf'][i]) > 60:
        (x, y, w, h) = (d['left'][i], d['top'][i], d['width'][i], d['height'][i])
        img = cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
cv2.imshow('img', img)
cv2.waitKey(0)

custom_config = r'-c tessedit_char_whitelist=abcdefghijklmnopqrstuvwxyz --psm 6'
print(pytesseract.image_to_string(img, config=custom_config))
