#!/usr/bin/env bash
# 测试图片
image_dir='data/HaGRID-test' # 测试图片的目录
weights="runs/yolov5s_640/weights/best.pt" # 模型文件
out_dir="runs/HaGRID-result" # 保存检测结果
python demo.py --image_dir $image_dir --weights $weights --out_diruns/yolov5s_640/weights/best.ptr $out_dir

# 测试视频文件
video_file="path/to/video.mp4" # 测试视频文件，如*.mp4,*.avi等
weights="runs/yolov5s_640/weights/best.pt" # 模型文件
out_dir="runs/HaGRID-result" # 保存检测结果
#python demo.py --video_file $video_file --weights $weights --out_dir $out_dir


# 测试摄像头
video_file=0 # 测试摄像头ID
#video_file = 'rtsp://admin:admin123@192.168.13.117:554/cam/realmonitor?channel=1&subtype=1'
weights="runs/yolov5s_640/weights/best.pt" # 模型文件
out_dir="runs/HaGRID-result" # 保存检测结果
#python demo.py --video_file $video_file --weights $weights --out_dir $out_dir
