#pip install ultralytics
from ultralytics import YOLO

# Load a model
model = YOLO("yolo11n.pt")

# Train the model
train_results = model.train(
    data="coco.yaml",  # path to dataset YAML
    epochs=10,  # number of training epochs
    imgsz=640,  # training image size
    device="0",  # device to run on, i.e. device=0 or device=0,1,2,3 or device=cpu
)

# Evaluate model performance on the validation set
metrics = model.val()

#Test or infer the image
model = YOLO("runs/detect/batch_size=16,epoch=20/best (2).pt")#weight to use

model.predict(r"C:\Users\user\Desktop\1.jpg", save=True, imgsz=1280, conf=0.5)