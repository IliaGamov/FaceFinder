import os
import time
import uuid
import cv2

#Path for progress
IMAGES_PATH = os.path.join('../data','images')
number_images = 90 #Number of images you want to create. This will be your dataset

cap = cv2.VideoCapture(0) #Allow this method to use your webcam
for imgnum in range(number_images):
    print('Collecting image {}'.format(imgnum)) #Printout progress
    ret, frame = cap.read()
    imgname = os.path.join(IMAGES_PATH,f'{str(uuid.uuid1())}.jpg') #Save images using uuid names
    cv2.imwrite(imgname, frame)
    cv2.imshow('frame', frame)
    time.sleep(0.5)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()

