# 基于YOLOv8的FPS/TPS AI自动锁定系统

## 1. 声明：

- 本项目仅供学习交流使用，不得用于商业用途，如有侵权请联系作者删除。

## 2. 项目简介：

- 本项目基于YOLOv8 [ultralytics YOLOv8](https://github.com/ultralytics/ultralytics)
- 通过YOLOv8-pose 关键点检测预训练模型，进一步进行自定义数据集训练，获取最佳射击点
- 使用c语言,win32 api编译的鼠标控制程序

## 3. 模型训练：

- 将自定义数据集放入dataset目录下，根据 ultralytics 官方文档进行训练 [ultralytics 官方文档](https://docs.ultralytics.com/tasks/pose/#models)

## 4. 使用方法：

- 安装依赖

```shell
pip install -r requirements.txt
```

- 运行main.py

```shell
python main.py
```


## 警告： 使用本项目产生的相应后果自负，作者不承担任何责任
