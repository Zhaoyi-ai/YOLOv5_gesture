# -*-coding: utf-8 -*-
"""
    @Author : panjq
    @E-mail : pan_jinquan@163.com
    @Date   : 2022-06-09 10:31:41
    @Brief  :
"""
import numpy as np
import utils.autoanchor as autoAC

if __name__ == "__main__":
    """
    YOLOv5s-640原始Anchor:
      - [10,13, 16,30, 33,23]  # P3/8
      - [30,61, 62,45, 59,119]  # P4/16
      - [116,90, 156,198, 373,326]  # P5/32
    YOLOv5s-640 Anchor:
    [[     24.734      39.921]
     [     35.297      57.048]
     [     47.535      72.372]
     [     55.251      100.37]
     [      75.29      87.114]
     [     71.389       126.3]
     [     98.448      120.22]
     [     103.17      169.94]
     [     161.11      194.18]]
    YOLOv5s-320:
    [[     12.665      19.416]
     [      17.38      28.171]
     [     22.806       34.51]
     [     25.526      47.696]
     [     33.645      41.292]
     [     34.557      59.526]
     [     49.253       54.79]
     [     46.538      79.431]
     [     70.809      92.732]]
    
    -  [12,19,  17,28, 22,34]
    -  [25,47,  33,41, 34,59]
    -  [49,54,  46,79, 70,92]
    """
    data = '/home/dm/nasdata/Detector/YOLO/yolov5/engine/configs/voc_local.yaml'
    anchors = autoAC.kmean_anchors(data, n=9, img_size=640, thr=5.0, gen=1000, verbose=True)
    anchors = np.asarray(anchors, dtype=np.int32)
    print(anchors)
    anchors = anchors.reshape(3, -1)
    print(anchors)
