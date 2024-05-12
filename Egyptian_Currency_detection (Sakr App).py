"""
Egyptian Currency detection App 𓂀 𓁈 𓀛 𓁀 𓁳 𓀮
        By: Omar Diab

Under the supervision of:
        Dr. Alaa Hamdy

Dataset i trained on: https://universe.roboflow.com/banha-university-dxs4z/egyptian-currency-psnkr/dataset/3      
        
>> The script will open the camera and start detecting the Egyptian currency in real-time.
>> THis Project Supports the following Currencies:  5 Pounds, 10 Pounds, 20 Pounds, 50 Pounds, 100 Pounds, 200 Pounds
>> The script will also display the total money detected in the frame.
>> Added a feature to speak the total money and the detected currencies when ['t'] is pressed.
>> Enjoy ^^
"""

# Import required libraries
import cv2
from ultralytics import YOLO
import pyttsx3
engine = pyttsx3.init()

# control the speed of the speech from there: -
engine.setProperty('rate', 200)

# set to highest volume 
engine.setProperty('volume', 1) 


# Load YOLO model
model = YOLO('Trained_Models/best_15e.pt')

# Initialize camera
cap = cv2.VideoCapture(0)  
#   >>>>> Note: If you want to use the another camera (eg: wireless), replace [0] with [1]

money = {10: "5 Pounds", 1: "5 Pounds", 0: "10 Pounds", 3: "10 Pounds", 9: "20 Pounds", 5: "20 Pounds", 8: "50 Pounds", 2: "50 Pounds", 4: "100 Pounds", 11: "100 Pounds", 6: "200 Pounds", 7: "200 Pounds"}

while True:
    ret, frame = cap.read()  # Read frame from camera


    # Add Gaussian blur to the frame (To Focus in important features only and reduce [Noise Features])
    model_frame = cv2.GaussianBlur(frame, (7, 7), 0)

    # Perform inference
    results = model.predict(source=model_frame, conf=0.5,verbose=False,save=False)

    # Track the total money
    total_money = 0
    money_positions=[]
    if results[0].boxes.cls.any():
        num_classes = len(results[0].boxes.cls)
        # Draw bounding boxes and class labels on the frame
        for box, conf, cls in zip(results[0].boxes.xyxy, results[0].boxes.conf, results[0].boxes.cls):
                x1, y1, x2, y2 = map(int, box)
                cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)  # Green color
                cls_index = int(cls.item())  # Extract class index as integer
                Currency = money[cls_index]  # Get currency name from labels dictionary

                cv2.putText(frame, f'{Currency} Acc: {conf:.2}', (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 250, 0), 2)
                
            # Calculate total money (sum of all detected currencies): -
                
                total_money += int(Currency.split()[0])
                money_positions.append((x1,Currency))  # Store x-coordinate of the currency boxq

        if total_money > 0: 
            cv2.putText(frame, f'Total Money: {total_money} Pounds', (10, 40), cv2.FONT_HERSHEY_TRIPLEX, 1, (0, 250, 0), 2)

            # Speak the total money and the detected currencies when 't' is pressed ^^
            if cv2.waitKey(1) & 0xFF == ord('t'):
                engine.say("Total Money: " + str(total_money)+" Pounds")
                engine.say("From Right to Left you have: ")
                sorted_money_positions = sorted(money_positions, key=lambda item: item[0], reverse=True)
                for x, y in sorted_money_positions:
                    engine.say(y)
                engine.runAndWait()


    cv2.imshow('Sakr: Egyptian Currency Detection', frame)

    # Press q to exit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release resources
cap.release()
cv2.destroyAllWindows()