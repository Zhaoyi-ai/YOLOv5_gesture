#!/usr/bin/env bash

#--------------训练yolov5s--------------
# 输出项目名称路径
project="runs/yolov5s"
# 训练和测试数据的路径
data="engine/configs/voc_local.yaml"
# YOLOv5模型配置文件
cfg="yolov5s.yaml"
# 训练超参数文件
hyp="data/hyps/hyp.scratch-v1.yaml"
# 预训练文件
weights="engine/pretrained/yolov5s.pt"
python train.py --data $data --cfg $cfg --hyp $hyp --weights $weights --batch-size 32 --imgsz 640 --workers 12 --project $project


#--------------训练轻量化版本yolov5s05--------------
# 输出项目名称路径
project="runs/yolov5s05"
# 训练和测试数据的路径
data="engine/configs/voc_local.yaml"
# YOLOv5模型配置文件
cfg="yolov5s05.yaml"
# 训练超参数文件
hyp="data/hyps/hyp.scratch-v1.yaml"
# 预训练文件
weights="engine/pretrained/yolov5s.pt"
python train.py --data $data --cfg $cfg --hyp $hyp --weights $weights --batch-size 32 --imgsz 320 --workers 12 --project $project
