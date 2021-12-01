import cv2
import imutils
from pygame import mixer
mixer.init()
mixer.music.load('C:\\Users\\User\\Downloads\\alarm.mp3')

hog = cv2.HOGDescriptor()
hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())

cap = cv2.VideoCapture('C:\\Users\\User\\Downloads\\638229886.mp4')

while cap.isOpened():
    
    ret, image = cap.read()
    if ret:
        image = imutils.resize(image,
                               width=min(400, image.shape[1]))

        (regions, _) = hog.detectMultiScale(image,
                                            winStride=(4, 4),
                                            padding=(4, 4),
                                            scale=1.05)
        if len(regions) > 0:
            mixer.music.play()

        for (x, y, w, h) in regions:
            cv2.rectangle(image, (x, y),
                          (x + w, y + h),
                          (0, 0, 255), 2)

        
        cv2.imshow("Image", image)
        if cv2.waitKey(25) & 0xFF == ord('q'):
            break
    else:
        break

cap.release()
cv2.destroyAllWindows()
         

