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
                    print(self.center_points)
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


tracker = EuclideanDistTracker()

cap = cv2.VideoCapture("Traffic Video 2.mov")

if not cap.isOpened():
    print("Cannot open stream")
    exit(1)

object_detector = cv2.createBackgroundSubtractorMOG2(history=100, varThreshold=40)

while True:
    ret, frame = cap.read()
    height, width, _ = frame.shape

    roi = frame[0:height, 0:width]

    mask = object_detector.apply(roi)
    _, mask = cv2.threshold(mask, 254, 255, cv2.THRESH_BINARY)
    contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    detections = []
    cars = cv2.CascadeClassifier("haarcascade_car.xml").detectMultiScale(frame, scaleFactor=1.1, minNeighbors=5)
    for (x, y, w, h) in cars:
        for cnt in contours:
            area = cv2.contourArea(cnt)
            if area > 100:
                # cv2.drawContours(roi, [cnt], -1, (0, 255, 0), 2)
                x2, y2, w2, h2 = cv2.boundingRect(cnt)

                if x2 >= x & x2 <= x + w:
                    detections.append([x, y, w, h])

    boxes_ids = tracker.update(detections)
    for box_id in boxes_ids:
        x, y, w, h, id = box_id
        # cv2.putText(roi, str(id), (x, y - 15), cv2.FONT_HERSHEY_PLAIN, 2, (255, 0, 0), 2)
        cv2.rectangle(roi, (x, y), (x + w, y + h), (0, 255, 0), 2)

    # cv2.imshow("roi", roi)
    cv2.imshow("Frame", frame)
    # cv2.imshow("Mask", mask)

    key = cv2.waitKey(30)
    if key == 27:
        break

cap.release()
cv2.destroyAllWindows()
