from ultralytics import YOLO

# 加载模型
model = YOLO("yolo11n.pt")

# 训练模型
train_results = model.train(
    data="dataset/100DOH/100doh.yaml",  # 数据集 YAML 路径
    epochs=100,  # 训练轮次
    batch=4,
    lr0=0.01,
    workers=0,
    device="0",  # 运行设备，例如 device=0 或 device=0,1,2,3 或 device=cpu
)
