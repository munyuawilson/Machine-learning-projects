import cv2

cap=cv2.VideoCapture(0)


while True:
    ret,frame=cap.read()
    cv2.imshow("freame",frame)
    
cap.release()

cv2.waitKey(0)
cv2.destroyAllWindows()