from ultralytics import YOLO

model = YOLO("runs/detect/batch_size=16,epoch=20/best (2).pt")

model.predict(r"image", save=True, imgsz=1280, conf=0.5)