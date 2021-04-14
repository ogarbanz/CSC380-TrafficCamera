import cv2
import math
import tkinter as tk
from tkinter import ttk
from tkinter import *
import tkinter.messagebox
import time


#tkinter window to get the input from thee user
class GetInput:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Get User Input")  #window title
        self.root.geometry("300x200+500+200")  #window geometry
        self.root.resizable(0,0)           #disable resizing
        self.root.configure(background='#4D4D4D')    
        s=ttk.Style(self.root)
        s.theme_use('xpnative')
        labe1 = tk.Label(self.root,foreground="#D6D6D6",background='#4D4D4D', text = 'Enter the distance in meter',
                          font=('Bold', 14)).place(x = 30, y = 10, width = 300, height = 70)
        self.entry1 = tk.Entry(self.root, width = 20, font = ('Arial', 12))
        self.entry1.place(x = 50, y = 55, height = 50)
        btn = tk.Button(self.root, text= "Submit", foreground="white",background='gray55',
            command=self.Submit)
        btn.place(x = 100, y = 110, width = 100, height = 50)

    def Submit(self):
        global flag, dis
        flag = 2
        #validate the user input
        try:
            dis = float(self.entry1.get())   #get distance in meter
            self.root.destroy()              #distroy the window after get the user input
        except:
            tkinter.messagebox.showerror(title="invalid input", message="You should Enter a number")

        
        

        

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

    
def drawrect(event,x,y,flags,param):    #handling the mouse event
    global points
    
    #append the four cornor point of the rectangle using the lift button of the mouse
    if event == cv2.EVENT_LBUTTONUP:     #event of relasing the left button of the mouse
        if len(points)<=4:
            points.append((x,y)) 


#intialize global variables    
dis =0             #distance in meter
points = []        #list of the rectangle points
flag = 0           #flag to show the window and clculate the distace in order
topAvg = (0,0)     #the midle point in the top of the rectangle
botAvg = (0,0)     #the midle point in the bottom of the rectangle
dis_pixel = 0      #the equladian distance between the above two points




tracker = EuclideanDistTracker()

cap = cv2.VideoCapture("highway.mp4")

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
    frame2 = frame.copy()
    key = cv2.waitKey(30)
    if key == 27:
        break
    elif key ==115 or key== 83:         #press s or S to select the rectangle
        cv2.setMouseCallback('Frame',drawrect)       #assign drawrect function to handle the mouse event
        
        orderdict = {1:"Top Left", 2:"Top Right",3:"Bottom Right",4:"Bottom Left",5:"Done"}    #user instruction
        
        while(1):
            
            j = cv2.waitKey(5) & 0xFF        #wait for input key
            if j == 117 or j == 85:    #press u or U to undo
                if(len(points)>0):
                    points.pop()       #delete last point
                    flag =0
                #print(points)

            elif j== 27:            #press Esq to return to the video recording
                break
            if(len(points)>0 and len(points)<=4):      
                for i in range(len(points)):
                    cv2.circle(frame,points[i],2,(0,0,255),2)      #draw circle in each corner
            if(len(points)==4):
                #draw rectangle
                for i in range(len(points)-1):
                    cv2.line(frame,points[i],points[i+1],(0,0,255),1)
                cv2.line(frame,points[0],points[-1],(0,0,255),1)
                flag +=1

                #draw the midle line
                topAvg = (int((points[0][0] + points[1][0])/2), int((points[0][1] + points[1][1])/2))
                botAvg = (int((points[2][0] + points[3][0])/2), int((points[2][1] + points[3][1])/2))
                #print(topAvg, botAvg)
                cv2.line(frame,topAvg,botAvg,(255,0,255),2)
            #put instruction text to the user
            cv2.putText(frame,orderdict[len(points)+1], (500,40), cv2.FONT_HERSHEY_SIMPLEX, .75, (255,0,255))
            cv2.putText(frame,"Press u to undo or Esc to continue recording", (400,20), cv2.FONT_HERSHEY_SIMPLEX, .75, (0,0,255))
            
            cv2.imshow("Frame", frame)   #update the freezing frame
            if(flag==1):
                #display the tkiner window to get the input from the user
                pba = GetInput()    
                pba.root.mainloop()
            if(flag==2):
                dis_pixel = math.sqrt((topAvg[0] - botAvg[0])**2 + (topAvg[1] - botAvg[1])**2)
                #print(dis_pixel)

            cv2.imshow("Frame", frame)
            frame = frame2.copy()
            

    #calculate speed
        for (x, y, w, h) in cars:
            if(x >= points[0][0] and y == points [0][1]):
                cv2.line(img, (points[0][0], points[0][1]), (points[1][0], points[1][1]), (0, 255,0), 2) #Changes color of the line
                time1 = time.time() #Initial time
                print("Car Entered")
                    
            if (x >= points[2][0] and y == points[2][1]):
                cv2.line(img, (points[2][0],points[2][1]), (points[3][0], points[3][1]), (0, 0, 255), 2)
                time2 = time.time()
                print("Car Left.")
                #We know that distance is 3m
                print("Speed in (m/s) is:", dis/((time2-time1)))

                    
             

cap.release()
cv2.destroyAllWindows()
