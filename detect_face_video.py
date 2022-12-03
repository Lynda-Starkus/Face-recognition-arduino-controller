import cv2
import serial as s
import time as t
# Load the cascade
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# To capture video from webcam. 
cap = cv2.VideoCapture(0)
# To use a video file as input 
# cap = cv2.VideoCapture('filename.mp4')
ser = s.Serial('com3', 9600, timeout=0)   # check your com port
t.sleep(2)
print(ser.name,"connected")


ser.write(b'0')    
print ("LED OFF")
while True:
    # Read the frame
    _, img = cap.read()

    # Convert to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Detect the faces
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)
    if len(faces) == 0:
            ser.write(b'0')    
            print ("LED OFF")  
    # Draw the rectangle around each face
    for (x, y, w, h) in faces:
        
        cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
        cv2.putText(img, 'Morad', (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255, 0, 0), 2)

        input_data = '1'
        print("Face detected")

        ser.write(b'1')
        print ("LED ON")

    # Display
    cv2.imshow('img', img)

    # Stop if escape key is pressed
    k = cv2.waitKey(30) & 0xff
    if k==27:
        break
    
# Release the VideoCapture object
cap.release()