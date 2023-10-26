# -*-coding: utf-8 -*-
"""
    @Author : panjq
    @E-mail : pan_jinquan@163.com
    @Date   : 2022-09-15 16:45:52
    @Brief  :
"""
import random
from pybaseutils import image_utils, file_utils, video_utils


def frame2gif():
    image_dir = "/home/dm/nasdata/Detector/YOLO/yolov5/runs/HaGRID-result"
    image_list = file_utils.get_images_list(image_dir)
    random.seed(100)
    random.shuffle(image_list)
    image_list = image_list[0:30]
    image_list = sorted(image_list)
    image_utils.image_file_list2gif(image_list, size=(416, 416), fps=2, loop=0, use_pil=True)


def video2gif():
    video_file = "/home/dm/nasdata/Detector/YOLO/yolov5/runs/HaGRID-result/手势识别Demo.avi"

    def target_task(frame):
        frame = image_utils.resize_image(frame, size=(None, 320))
        return frame

    video_utils.video2gif(video_file, gif_file=None, func=target_task, interval=10, use_pil=False, vis=True)


if __name__ == "__main__":
    # frame2gif()
    video2gif()
