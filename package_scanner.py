import cv2
from gpiozero import Servo
from time import sleep
from smbus import SMBus


# qr code scanner setup
cap = cv2.VideoCapture(0)
detector = cv2.QRCodeDetector()

# i2c setup values.
addr = 0x8 # bus address.
bus = SMBus(1) # Indicates /dev/i2c-1

while True:
    # Runs the qr code scanner and camera.
    _, img = cap.read()
    data, bbox, _ = detector.detectAndDecode(img)
    
    if(bbox is not None):
        for i in range(len(bbox)):
            cv2.line(img, tuple(bbox[i][0]), tuple(bbox[(i+1) % len(bbox)][0]), color=(255,
                     0, 255), thickness=2)
        cv2.putText(img, data, (int(bbox[0][0][0]), int(bbox[0][0][1]) - 10), cv2.FONT_HERSHEY_SIMPLEX,
                    0.5, (0, 255, 0), 2)

        print("data found: ", data)
        if data:
            if data == "nsw":
                message = 0
            if data == "vic":
                message = 1
            bus.write_byte(addr, message)
            data = ""

    cv2.imshow("code detector", img)
    if(cv2.waitKey(1) == ord("q")):
        break
cap.release()
cv2.destroyAllWindows()

