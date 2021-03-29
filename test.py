import tkinter as tk

root = tk.Tk()
root.title("Traffic Camera")
root.iconbitmap('car_icon.ico')

width, height = root.winfo_screenwidth(), root.winfo_screenheight()
root = tk.Canvas(root, width=width, height=height)
root.configure(bg='#FFFFFF')
root.pack()

if __name__ == '__main__':
    mics_info = tk.Label(root, bg='#FFFFFF', text="Location/Date/Time", font=('', 12))
    root.create_window(width/4, height/8, anchor='sw', window=mics_info)

    root.create_rectangle(width/4, height/8, width/4*3, height/8*6)
    root.create_line(width/4, height/8, width/4*3, height/8*6)
    root.create_line(width/4*3, height/8, width/4, height/8*6)
    video_feed = tk.Label(root, bg='#FFFFFF', text="Video Feed", font='bold')
    root.create_window(width/2, height/16*7, anchor='center', window=video_feed)

    speedLimit = tk.Label(root, bg='#FFFFFF', text="Speed Limit: 25 mph", font=('', 12))
    root.create_window(width/4, height/8*6+1, anchor='nw', window=speedLimit)

    email = tk.Label(root, bg='#FFFFFF', text="Email: example@web.com", font=('', 12))
    root.create_window(width/4*3, height/8*6+1, anchor='ne', window=email)

    settings_button = tk.Button(text='Settings', width=10, font=('', 12))
    root.create_window(width/2-20, height/8*7, anchor='e', window=settings_button)

    help_button = tk.Button(text='Help', width=10, font=('', 12))
    root.create_window(width/2+20, height/8*7, anchor='w', window=help_button)
    
    root.mainloop()
