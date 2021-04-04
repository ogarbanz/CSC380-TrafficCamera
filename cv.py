import cv2

vid = cv2.VideoCapture("Traffic Video.mov")
# out = cv2.VideoWriter("Traffic Video Cascade.mov", -1, 30, (568, 320))

if not vid.isOpened():
    print("Cannot open stream")
else:
    i = 0
    while True:
        ret, frame = vid.read()

        cars = cv2.CascadeClassifier("haarcascade_car.xml").detectMultiScale(frame, scaleFactor=1.15, minNeighbors=8)

        for (x, y, w, h) in cars:
            quart = int(h / 4)
            cv2.rectangle(frame, (x, y + quart), (x + w, y + (quart * 3)), (0, 255, 15), 2)

        cv2.imshow("Frame", frame)
        # out.write(frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    vid.release()
    # out.release()
    cv2.destroyAllWindows()
