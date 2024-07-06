# Egyptian Currency Detection 𓂀 𓁈 𓀛 𓁀 𓁳 𓀮 

The application uses **YoloV8 model** to detect Egyptian currencies in real-time using a camera feed.


## Features

- **Real-Time Detection:** The script opens the camera feed and continuously detects Egyptian currency notes within the frame.
- **Total Money Display:** It displays the total sum of money detected in the frame.

<div style="display: flex; justify-content: center; align-items: center;">
    
<img src="https://github.com/OmarMDiab/Sakr-Egyptian-Currency-Detection/blob/main/Sample_Runs/Counting_Currency.gif" alt="Sample Run" height = 350/>
</div>


  

- **Text-to-Speech Feature:** Pressing the 't' key triggers a feature that audibly announces the total amount of money detected and lists the detected currencies from right to left (relative to the camera)

### [See Also, Sound Feedback (Video)](https://drive.google.com/file/d/12EAiGe2aaU_pwLoC-RN-uz6NkXMH03Xr/preview)

<video width="640" height="480" controls autoplay>
  <source src="Sample_Runs/Sound_Feedback.mp4" type="video/mp4">
</video>






## Dataset
The model was trained on the 
[Banha University Egyptian Currency Dataset ](https://universe.roboflow.com/banha-university-dxs4z/egyptian-currency-psnkr/dataset/3)available on Roboflow Universe.

## what you need to install first
- **OpenCV:** To use your camera for detection
- **Ultralytics YOLO (ultralytics):** To use/Train the YoloV8 Model
- **pyttsx3:** To get the Sound Feedback

