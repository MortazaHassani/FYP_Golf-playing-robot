import cv2
import json

with open('setting.json') as jfile:
    setting =json.load(jfile)
    

# Open the video capture
cap = cv2.VideoCapture(0, cv2.CAP_V4L2)  # Use 0 for the default camera

# Set the desired resolution
width = setting['camera']['width']
height = setting['camera']['height']
cap.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
cap.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc('M', 'J', 'P', 'G'))
cap.set(cv2.CAP_PROP_FPS, setting['camera']['FPS'])


# Check if the resolution was set successfully
print("Actual Resolution: {} x {} & FPS: {}".format(cap.get(cv2.CAP_PROP_FRAME_WIDTH), cap.get(cv2.CAP_PROP_FRAME_HEIGHT),cap.get(cv2.CAP_PROP_FPS)))

# Start capturing and displaying frames
while True:
    ret, frame = cap.read()
    
    # Perform any processing or display operations here
    
    cv2.imshow("Webcam", frame)
    
    # Exit the loop if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the video capture and close any open windows
cap.release()
cv2.destroyAllWindows()
