import cv2
import numpy

cap=cv2.VideoCapture(0)

while cap.isOpened():
    success,frame =cap.read()
   
    if success:
        gray_frame=cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        cv2.imshow("gray frame ", gray_frame)
        cv2.imshow("actual image",frame)
        
        k=cv2.waitKey(1)
        if k & 0xff == ord("q"):
            break
        
    else:
        break
cap.release()
cv2.destroyAllWindows()
