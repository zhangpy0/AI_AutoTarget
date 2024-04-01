from ultralytics import YOLO
import numpy as np


def find_center_point(points):
    try:
        if len(points) == 0:
            return None
        elif len(points) == 1:
            return np.array(points[0][0])
        else:
            # 选择最接近640, 400
            target = np.array([640, 400])
            min_dis = np.inf
            for point in points:
                point = np.array(point[0])
                if np.linalg.norm(point - target) < min_dis:
                    min_dis = np.linalg.norm(point - target)
                    center_point = point
            return center_point
    except Exception as e:
        print(e)
        return None

class YOLOPre:
    def __init__(self):
        self.model = YOLO('yolov8n-pose.pt')
        self.model = YOLO('runs/pose/train2/weights/best.pt')

    def prehot(self, img):
        results = self.model(img)
        shot_points = results[0].keypoints.xy.numpy()
        return find_center_point(shot_points)
    
    # img: opencv_mat
    def bestshot(self, img):
        results = self.model(img)
        shot_points = results[0].keypoints.xy.numpy()
        return find_center_point(shot_points)

if __name__ == '__main__':
    def main():
        yolo_pre = YOLOPre()
        print(yolo_pre.prehot('dataset/test/images'))
        import cv2
        import time
        import os
        dir_name = 'taged'
        for img in os.listdir(dir_name):
            img = os.path.join(dir_name, img)
            print(img)
            img = cv2.imread(img)
            now = time.time()
            print(yolo_pre.bestshot(img))
            print('Time elapsed:', time.time() - now)

    main()
