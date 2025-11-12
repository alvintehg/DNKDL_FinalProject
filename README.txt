1.Prerequisites
(1). Install PyCharm OR Jupyter Lab in your computer before run our file.
a. Install PyCharm:
	link:https://www.jetbrains.com/pycharm/download/?section=windows
b. Install JupyterLab with pip:
	pip install jupyterlab
Environment Setup:
(3). Install Python (version >= 3.7 recommended).
(4). Install the necessary dependencies:
     pip install ultralytics.


2. We have already save our outputs in /runs/detect/batch_size=32, /runs/detect/batch_size=16 and  /runs/detect/batch_size=16 epoch=20. you can use "best.pt" to predict.

3. Running Code Tutorial
Using link below to download Our Group "DNKDL" code "yolov11.zip" file 
Link:
https://xmueducn-my.sharepoint.com/:u:/g/personal/dsc2209255_xmu_edu_my/EZBkAIb4F8hNhNMS_mooyeMBmLG7q1pJTd7_wH4-nU6pfQ?e=acw0Mq

After download our "yolov11.zip" code file, extract it and open it in PyCharm/Jupyter Lab. 

Open "main.py" ,which is a combination of train.py and test.py (they are also in the file).

We recommend you to use train.py for training and test.py for detecting.

If you don't want to modify anything, you only need to run train.py for training and test.py for detecting.
Else you need to follow the instructions bellow:
Due to the large size of "coco2017" dataset, you can change "coco.yaml" to "coco8.yaml" for post training as well as fine-tuning, which is much more smaller.

4. Training the YOLO Model
Instructions:
(1). Replace "coco.yaml" with the path to your dataset's YAML file.
Due to the large size of coco2017, you can change coco.yaml to coco8.yaml for post training as well as fine-tuning, which is much more smaller.

Modify the following parameters in the training script(if you want):
(2). epochs: Set the desired number of training iterations.
(3). imgsz: Adjust the image size for better accuracy or performance.
(4). device: Set to "0" for GPU or "cpu" for running on a CPU.
Output:
After training, the model saves weights in the "runs/train/weights" folder.

5. Running Predictions
Instructions:
(1). Replace the model path (best.pt) with the file path to your trained weights.
(2). Replace the "source" parameter with the path to your input image or video..
Adjust the following parameters for better prediction results:
(3). imgsz: Image size.
(4). conf: Confidence threshold.
(5). Set "save=True" to save the annotated prediction image.
Output:
The annotated prediction results are saved in the "runs/detect" folder.