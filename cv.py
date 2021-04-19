import time
from datetime import datetime
from multiprocessing import Process
import cv2
import math


class EuclideanDistTracker:
    def __init__(self):
        self.center_points = {}
        self.id_count = 0

    def update(self, objects_rect):
        objects_bbs_ids = []

        for rect in objects_rect:
            x, y, w, h = rect
            cx = (x + x + w) // 2
            cy = (y + y + h) // 2

            same_object_detected = False
            for id, pt in self.center_points.items():
                dist = math.hypot(cx - pt[0], cy - pt[1])

                if dist < 25:
                    self.center_points[id] = (cx, cy)
                    # print(self.center_points)
                    objects_bbs_ids.append([x, y, w, h, id])
                    same_object_detected = True
                    break

            if same_object_detected is False:
                self.center_points[self.id_count] = (cx, cy)
                objects_bbs_ids.append([x, y, w, h, self.id_count])
                self.id_count += 1

        new_center_points = {}
        for obj_bb_id in objects_bbs_ids:
            _, _, _, _, object_id = obj_bb_id
            center = self.center_points[object_id]
            new_center_points[object_id] = center

        self.center_points = new_center_points.copy()
        return objects_bbs_ids


def start_stream():
    tracker = EuclideanDistTracker()
    email_send_time = datetime.now()
    frames = []
    speeds = []

    cap = cv2.VideoCapture("Traffic Video.mov")

    if not cap.isOpened():
        print("Cannot open stream")
        exit(1)

    while True:
        _, frame = cap.read()
        speed = 0

        if frame is None:
            break

        detections = []
        cars = cv2.CascadeClassifier("haarcascade_car.xml").detectMultiScale(frame, scaleFactor=1.15, minNeighbors=6)
        for (x, y, w, h) in cars:
            detections.append([x, y, w, h])

        boxes_ids = tracker.update(detections)
        if not len(boxes_ids) == 0:
            curr_id = boxes_ids[0][4]
            curr_x = boxes_ids[0][0]
            curr_y = boxes_ids[0][1]
            curr_time = datetime.now().second
            if not len(frames) == 0:
                if frames[len(frames) - 1][0] == curr_id:
                    x_dis_sqr = math.pow(curr_x - frames[0][1], 2)
                    y_dis_sqr = math.pow(curr_y - frames[0][2], 2)
                    distance = math.sqrt(x_dis_sqr + y_dis_sqr)
                    if curr_time > frames[0][3]:
                        speed = ((distance / (curr_time - frames[0][3])) * 2.236936) + 10
                        speed = round(speed, 2)
                        speeds.append(speed)
                        if len(speeds) > 1:
                            speed = 0
                            for curr_speed in speeds:
                                speed += curr_speed
                            speed /= len(speeds)
                            speed = round(speed, 2)
                        time_diff = datetime.now() - email_send_time
                        if speed > 20 and int(time_diff.total_seconds()) > 5:
                            email_send_time = datetime.now()
                            print("SPEED EXCEEDED!")
                    frames.append([curr_id, curr_x, curr_y, curr_time])
                else:
                    frames = [[curr_id, curr_x, curr_y, curr_time]]
                    speeds = []
            else:
                frames.append([curr_id, curr_x, curr_y, curr_time])

        for box_id in boxes_ids:
            x, y, w, h, id = box_id
            if speed > 0:
                cv2.putText(frame, str(speed), (x, y - 15), cv2.FONT_HERSHEY_PLAIN, 2, (255, 0, 0), 2)
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

        cv2.imshow("Traffic Camera", frame)

        if cv2.waitKey(30) == 27:
            break

    cap.release()
    cv2.destroyAllWindows()
