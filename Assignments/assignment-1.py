import cv2
# import numpy as np

cap=cv2.VideoCapture(0)
smiley=cv2.imread("smiley.png")
colorful_bg=cv2.imread("background.jpg")
goku=cv2.imread("goku.jpg")

print("enter the filter that you want to apply:\n 1. smiley \n 2. gradient background \n 3. goku \n 4. Waterfall effect \n 5. blue effect \n 6.environment_effect ")
inp=int(input())
if inp == 1:
    image=cv2.imread('smiley.png')
elif inp ==2:
    image=cv2.imread('background.jpg')
elif inp ==3:
    image=cv2.imread('goku.jpg')
elif inp ==4:
    image=cv2.imread('env.jpg')
elif inp ==5:
    image=cv2.imread('win11.jpg')
else:
    image=cv2.imread('natureee.jpg')
while True:
    success,frame=cap.read()
    if not success:
        print("couldn't access camera")
        break
    image=cv2.resize(image,(frame.shape[1],frame.shape[0]))
    if inp==4 or inp==5 or inp==6:
        blended_frame= cv2.addWeighted(image,0.4,frame,0.6,gamma=0.1)
    else:
        blended_frame= cv2.addWeighted(image,0.2,frame,0.8,gamma=0.1)
 
    cv2.imshow("fi;ters ",blended_frame)
    if cv2.waitKey(1) & 0xff ==ord('q'):
        break

cap.release()
cv2.destroyAllWindows() 
