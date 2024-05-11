# Egyptian Currency Detection 𓂀 𓁈 𓀛 𓁀 𓁳 𓀮 

The application uses **our trained YoloV8 model** to detect Egyptian currency denominations in real-time using a camera feed.


## Features
- **Real-Time Detection:** The script opens the camera feed and continuously detects Egyptian currency notes within the frame.


- **Total Money Display:** It displays the total sum of money detected in the frame.

- **Text-to-Speech Feature:** Pressing the **'t'** key triggers a feature that audibly announces the total amount of money detected and lists the detected currencies from right to left.

## See this video ==>  [Talkative Currency Detection Video](https://drive.google.com/file/d/12ITHoKfdFgiIFR23oXIu5Y4Co4MBtRlI/view?usp=sharing)




## Dataset
The model was trained on the 
[Banha University Egyptian Currency Dataset ](https://universe.roboflow.com/banha-university-dxs4z/egyptian-currency-psnkr/dataset/3)available on Roboflow Universe.

## what you need to install first
- **OpenCV**
- **Ultralytics YOLO (ultralytics)**
- **pyttsx3**

## Authors
- **Omar Diab**
- Under the supervision of **Dr. Alaa Hamdy.** 
