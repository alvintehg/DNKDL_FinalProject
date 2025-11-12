# DNKDL YOLOv11 Project

This project implements object detection using YOLOv11 (Ultralytics) for training and inference.

## Prerequisites

### 1. Install Development Environment

Choose one of the following:

**Option A: PyCharm**
- Download from: https://www.jetbrains.com/pycharm/download/?section=windows

**Option B: JupyterLab**
```bash
pip install jupyterlab
```

### 2. Environment Setup

1. Install Python (version >= 3.7 recommended)
2. Install the necessary dependencies:
```bash
pip install ultralytics
```

## Project Structure

Pre-trained model outputs are saved in:
- `/runs/detect/batch_size=32`
- `/runs/detect/batch_size=16`
- `/runs/detect/batch_size=16 epoch=20`

You can use `best.pt` from these directories for predictions.

## Getting Started

### Download the Code

Our complete code package is available here:
[Download yolov11.zip](https://xmueducn-my.sharepoint.com/:u:/g/personal/dsc2209255_xmu_edu_my/EZBkAIb4F8hNhNMS_mooyeMBmLG7q1pJTd7_wH4-nU6pfQ?e=acw0Mq)

After downloading:
1. Extract the `yolov11.zip` file
2. Open the project in PyCharm or Jupyter Lab

### Running the Code

The project includes three main Python files:

- **`main.py`**: Combined training and testing script
- **`train.py`**: Dedicated training script (recommended for training)
- **`test.py`**: Dedicated detection/inference script (recommended for testing)

**Quick Start**: If you don't want to modify anything, simply run:
- `train.py` for training
- `test.py` for detecting

## Training the YOLO Model

### Dataset Configuration

Due to the large size of the COCO2017 dataset, you can use the smaller COCO8 dataset for training and fine-tuning:
- Replace `coco.yaml` with `coco8.yaml` in your training script

### Training Parameters

Modify the following parameters in the training script as needed:

| Parameter | Description | Example |
|-----------|-------------|---------|
| `data` | Path to dataset YAML file | `coco8.yaml` |
| `epochs` | Number of training iterations | `50`, `100` |
| `imgsz` | Image size for training | `640`, `1280` |
| `device` | Computing device | `"0"` (GPU) or `"cpu"` |

### Training Output

After training completes, model weights are saved in:
```
runs/train/weights/
```

## Running Predictions

### Basic Usage

1. Update the model path to your trained weights:
   ```python
   model = YOLO('path/to/best.pt')
   ```

2. Set the source (image or video path):
   ```python
   results = model.predict(source='path/to/image.jpg')
   ```

### Prediction Parameters

Adjust these parameters for better results:

| Parameter | Description | Default |
|-----------|-------------|---------|
| `imgsz` | Image size | `640` |
| `conf` | Confidence threshold | `0.25` |
| `save` | Save annotated results | `True` |

### Prediction Output

Annotated prediction results are saved in:
```
runs/detect/
```

## License

This project uses the Ultralytics YOLOv11 framework. Please refer to the Ultralytics license for usage terms.

## Contact

Project by: DNKDL Group
