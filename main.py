import cv2 as cv

"""
img = cv.imread("cat.jpg")

cv.imshow("Cat",img)


"""
#Video
capture = cv.VideoCapture(0)

while True:
    isTrue, frame = capture.read()
    cv.imshow("Video", frame)
cv.waitKey(0)

