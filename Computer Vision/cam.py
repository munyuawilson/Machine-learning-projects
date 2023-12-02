import cv2

cap=cv2.VideoCapture(1)


while True:
    ret,frame=cap.read()
    cv2.imshow("frame",frame)
    
    cv2.imwrite("fff.png",frame)
    
cap.release()

cv2.waitKey(0)
cv2.destroyAllWindows()
