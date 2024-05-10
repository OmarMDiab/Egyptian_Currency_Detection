"""
>> This file is used to test the model through a single image.
"""


from ultralytics import YOLO

# Load YOLO model
model = YOLO('weights/best_15e.pt')

# Run inference on image
results = model.predict(source='Single_Sample_image.jpg', conf=0.1,save=True)