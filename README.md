# YOLOv11 for hand detection
This is a model trained for detecting hands in photos based on YOLOv11.

## Dataset
We used the 100DOH as the train&val set.

## Quickly start
If you want to use the model we trianed directly, please follow the steps:

### 1.download the code
```
git clone https://github.com/sunnygit2005/YOLOv11_4_hands
```

### 1.create the virtual env
We suggest to use the python=3.9:
```
conda create -n yolov11 python=3.9
```

### 2.install the packages
```
pip install -r requirements.txt
```

### 3.try the detect task
The model was stored in hand_model/weights/best.pt, and you can do a test by following this:
```
cd ./ultralytics
yolo predict model=hand_model/weights/best.pt source=test_photos/test_hand1.jpg
```

Of course you can do other task by reading the director docs of the original work of YOLOv11
@https://github.com/ultralytics/ultralytics
