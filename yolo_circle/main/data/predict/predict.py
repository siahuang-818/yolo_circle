from ultralytics import YOLO

# 加载训练好的模型
model = YOLO(r'C:\Python\PythonProject\yolo_circle\main\runs\detect\train15\weights\best.pt')

# 使用模型进行预测
results = model.predict(source=r'C:\Python\PythonProject\yolo_circle\main\data\predict\video', save=True)