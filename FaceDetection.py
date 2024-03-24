import cv2

alg = 'data/haarcascade_frontalface_default.xml'

cascade = cv2.CascadeClassifier(alg)

cam = cv2.VideoCapture(0)
if not cam.isOpened():
    print("Error opening camera (default)")
    cam = cv2.VideoCapture(1)

if not cam.isOpened():
    print("Error opening all cameras")
    exit()

while True:
    
    _,img = cam.read()
    
    grayImg = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

    face = cascade.detectMultiScale(grayImg)

    for (x, y, w, h) in face:
        
        cv2.rectangle(img, (x, y), (x + w, y + h),(0,255,0),2)

    cv2.imshow("FaceDetect",img)

    key = cv2.waitKey(1)

    if key == 81 or key == 113 :
        break

cam.release()
cv2.destroyAllWindows()