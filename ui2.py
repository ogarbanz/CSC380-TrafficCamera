from datetime import date
from datetime import datetime
import tkinter as tk

root = tk.Tk()
root.title("Traffic Camera")
root.geometry("+0+0")
root.iconbitmap('car_icon.ico')

width, height = root.winfo_screenwidth(), root.winfo_screenheight()
root = tk.Canvas(root, width=width, height=height)
root.configure(bg='#FFFFFF')
root.pack()


def main():
    global state, user_email, user_speed, user_location, rec, line1, line2, settings_button, help_button

    for widget in root.winfo_children():
        widget.destroy()
    if state == "settings":
        email_save.destroy()
        speed_save.destroy()
        location_save.destroy()
        back_button.destroy()
    elif state == "help":
        back_button.destroy()
    state = "main"

    time = str(datetime.time(datetime.now()).hour) + ":" + str(datetime.time(datetime.now()).minute)
    mics_info = tk.Label(root, bg='#FFFFFF', text=user_location + " / " + str(date.today()) + " / " + time, font=('', 12))
    root.create_window(width/4, height/8, anchor='sw', window=mics_info)

    rec = root.create_rectangle(width/4, height/8, width/4*3, height/8*6)
    line1 = root.create_line(width/4, height/8, width/4*3, height/8*6)
    line2 = root.create_line(width/4*3, height/8, width/4, height/8*6)
    video_feed = tk.Label(root, bg='#FFFFFF', text="Video Feed", font='bold')
    root.create_window(width/2, height/16*7, anchor='center', window=video_feed)

    speed_limit = tk.Label(root, bg='#FFFFFF', text="Speed Limit: " + str(user_speed) + " mph", font=('', 12))
    root.create_window(width/4, height/8*6+1, anchor='nw', window=speed_limit)

    email = tk.Label(root, bg='#FFFFFF', text="Email: " + user_email, font=('', 12))
    root.create_window(width/4*3, height/8*6+1, anchor='ne', window=email)
    settings_button = tk.Button(text='Settings', width=10, font=('', 12), command=settings)
    root.create_window(width/2-20, height/8*7, anchor='e', window=settings_button)

    help_button = tk.Button(text='Help', width=10, font=('', 12), command=help)
    root.create_window(width/2+20, height/8*7, anchor='w', window=help_button)


def settings():
    global state, user_email, user_speed, user_location, email_field, speed_field, location_field, \
        email_save, speed_save, location_save, back_button

    for widget in root.winfo_children():
        widget.destroy()
    root.delete(rec)
    root.delete(line1)
    root.delete(line2)
    settings_button.destroy()
    help_button.destroy()
    state = "settings"

    settings_title = tk.Label(root, bg='#FFFFFF', text="Settings", font=('', 12))
    root.create_window(width/2, height/20, anchor='center', window=settings_title)

    email_label = tk.Label(root, bg='#FFFFFF', text="Email", font=('', 12))
    root.create_window(width/2-100, height/20*3, anchor='e', window=email_label)
    email_field = tk.Entry(root, width=30, bd=3)
    root.create_window(width/2, height/20*3, anchor='center', window=email_field)

    email_save = tk.Button(text='Save', width=10, font=('', 12), command=save_email)
    root.create_window(width/5*3, height/20*3, anchor='w', window=email_save)

    speed_label = tk.Label(root, bg='#FFFFFF', text="Speed Limit", font=('', 12))
    root.create_window(width/2-100, height/20*4.5, anchor='e', window=speed_label)
    speed_field = tk.Entry(root, width=30, bd=3)
    root.create_window(width/2, height/20*4.5, anchor='center', window=speed_field)

    speed_save = tk.Button(text='Save', width=10, font=('', 12), command=save_speed)
    root.create_window(width/5*3, height/20*4.5, anchor='w', window=speed_save)

    location_label = tk.Label(root, bg='#FFFFFF', text="Location", font=('', 12))
    root.create_window(width/2-100, height/20*6, anchor='e', window=location_label)
    location_field = tk.Entry(root, width=30, bd=3)
    root.create_window(width/2, height/20*6, anchor='center', window=location_field)

    location_save = tk.Button(text='Save', width=10, font=('', 12), command=save_location)
    root.create_window(width/5*3, height/20*6, anchor='w', window=location_save)

    back_button = tk.Button(text='Back', width=10, font=('', 12), command=main)
    root.create_window(width/2, height/20*8, anchor='center', window=back_button)


def help():
    global state, back_button

    for widget in root.winfo_children():
        widget.destroy()
    root.delete(rec)
    root.delete(line1)
    root.delete(line2)
    settings_button.destroy()
    help_button.destroy()
    state = "help"

    help_title = tk.Label(root, bg='#FFFFFF', text="Help", font=('', 12))
    root.create_window(width/2, height/20, anchor='center', window=help_title)

    getting_started = tk.Label(root, bg='#FFFFFF', text="Getting Started", font=('', 12))
    root.create_window(width/2, height/20*3, anchor='center', window=getting_started)

    s_text = """Upon starting the program, you will be greeted by the home
        page of the Traffic Camera software. Here, you can view the live feed 
        of the traffic camera, its location, its speed threshold, the email, 
        as well as the time and date. At the bottom of the 
        screen are two buttons which allow access to the settings page and the 
        help page."""
    start_text = tk.Label(root, bg='#FFFFFF', text=s_text, font=('', 12))
    root.create_window(width/2, height/20*4, anchor='n', window=start_text)

    settings = tk.Label(root, bg='#FFFFFF', text="Settings", font=('', 12))
    root.create_window(width/2, height/20*9, anchor='center', window=settings)

    settings_text = """Upon clicking the 'Settings' button on the home page, 
        a window will be presented giving you a couple options that allow
        modification. The first text box allows you to manipulate the current
        email that will be notified. The second text box allows you to 
        manipulate the speed threshold of the traffic camera. The third text box 
        allows you to manipulate the current location of the traffic camera. 
        Clicking on the 'Save' button next to these text boxes modifies the value
        of the respective text box. Once your changes are complete, 
        clicking on the 'Back' button will bring you back to the home page, where 
        the updated information will be displayed."""
    settings_label = tk.Label(root, bg='#FFFFFF', text=settings_text, font=('', 12))
    root.create_window(width/2, height/20*10, anchor='n', window=settings_label)

    back_button = tk.Button(text='Back', width=10, font=('', 12), command=main)
    root.create_window(width/2, height/20*16, anchor='center', window=back_button)


def save_email():
    global user_email, email_field
    user_email = email_field.get()


def save_speed():
    global user_speed, speed_field
    user_speed = speed_field.get()


def save_location():
    global user_location, location_field
    user_location = location_field.get()


if __name__ == '__main__':
    global state, user_email, user_speed, user_location
    user_email = "example@web.com"
    user_speed = 25
    user_location = "Location"
    state = "main"
    main()
    root.mainloop()
