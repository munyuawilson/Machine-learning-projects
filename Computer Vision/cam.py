import cv2
video_writer = cv2.VideoWriter('output.avi', cv2.VideoWriter_fourcc(*'XVID'), 20.0, (640, 480))
cap=cv2.VideoCapture(0)


while True:
    ret,frame=cap.read()
    #cv2.imshow("frame",frame)
    video_writer.write(frame)
    
    
    
cap.release()

cv2.waitKey(0)
cv2.destroyAllWindows()
