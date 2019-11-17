# import time
# import cv2
# import mss
# import numpy

# with mss.mss() as sct:
#     # Part of the screen to capture
#     monitor = {"top": 700, "left": 1540, "width": 400, "height": 400}

#     while "Screen capturing":
#         last_time = time.time()
#         # Get raw pixels from the screen, save it to a Numpy array
#         img = numpy.array(sct.grab(monitor))

#         # Display the picture
#         cv2.imshow("OpenCV/Numpy normal", img)

#         # Display the picture in grayscale
#         # cv2.imshow('OpenCV/Numpy grayscale',
#         #            cv2.cvtColor(img, cv2.COLOR_BGRA2GRAY))

#         # print("fps: {}".format(1 / (time.time() - last_time)))

#         # Press "q" to quit
#         if cv2.waitKey(2000) & 0xFF == ord("q"):
#             cv2.destroyAllWindows()
#             break


import cv2
import numpy as np
import urllib.request


url = 'http://ddragon.leagueoflegends.com/cdn/9.21.1/img/champion/LeeSin.png'


img_rgb = cv2.imread('asdad.png')


img_gray = cv2.cvtColor(img_rgb, 0)

template = cv2.imread('Darius.png', 0)

template2 = cv2.resize(template, (25, 25))

w, h = template2.shape[::-1]

res = cv2.matchTemplate(img_gray, template2, cv2.TM_CCOEFF_NORMED)
threshold = 0.4
loc = np.where(res >= threshold)

for pt in zip(*loc[::-1]):
    cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0, 255, 255), 2)

cv2.imshow('Detected', template2)
cv2.waitKey(5000)
