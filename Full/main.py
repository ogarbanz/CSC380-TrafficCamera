import tkinter as tk
import tkinter.messagebox
import tkinter.filedialog
import webbrowser
import os
import re
import cv


def settings():
    global state, start_button, help_button, load_file_button, email_field, speed_field, location_field

    for widget in window.winfo_children():
        widget.destroy()
    if state == "help":
        back_button.destroy()
        github_button.destroy()
        window.delete(border)
        window.delete(horizon)
        window.delete(left_road)
        window.delete(right_road)
        window.delete(middle_road)
    state = "settings"

    settings_title = tk.Label(window, bg='#235937', text="Settings", font=('', 12, 'bold'), fg='#FFE86E')
    window.create_window(250, 20, anchor='center', window=settings_title)

    email_label = tk.Label(window, bg='#235937', text="Email", font=('', 12), fg='#FFFFFF')
    window.create_window(150, 80, anchor='e', window=email_label)
    email_field = tk.Entry(window, width=30, bd=3)
    window.create_window(155, 80, anchor='w', window=email_field)

    speed_label = tk.Label(window, bg='#235937', text="Speed Limit", font=('', 12), fg='#FFFFFF')
    window.create_window(150, 120, anchor='e', window=speed_label)
    speed_field = tk.Entry(window, width=30, bd=3)
    window.create_window(155, 120, anchor='w', window=speed_field)

    location_label = tk.Label(window, bg='#235937', text="Location", font=('', 12), fg='#FFFFFF')
    window.create_window(150, 160, anchor='e', window=location_label)
    location_field = tk.Entry(window, width=30, bd=3)
    window.create_window(155, 160, anchor='w', window=location_field)

    start_button = tk.Button(text="Start", width=10, font=('', 12), command=start_stream)
    window.create_window(230, 240, anchor='e', window=start_button)

    help_button = tk.Button(text="Help", width=10, font=('', 12), command=help)
    window.create_window(270, 240, anchor='w', window=help_button)

    note_text = "Note:\nExit the video feed by pressing the ESC key\non the keyboard"
    note_label = tk.Label(window, bg='#235937', text=note_text, font=('', 12, 'bold'), fg='#FCE86E')
    window.create_window(250, 300, anchor='n', window=note_label)

    load_file_text = "Click \"Load File\" to load a pre-recorded video.\n" \
                       "Otherwise, the program will start with live video feed."
    load_file_label = tk.Label(window, bg='#235937', text=load_file_text, font=('', 12), fg='#FFFFFF')
    window.create_window(250, 400, anchor='n', window=load_file_label)

    load_file_button = tk.Button(text="Load File", width=10, font=('', 12), command=load_file)
    window.create_window(250, 470, anchor='center', window=load_file_button)


def load_file():
    global file
    file = tk.filedialog.askopenfile(filetype=[("*.mov *.mp4", ["*.mov", "*.mp4"])]).name


def help():
    global state, back_button, github_button, border, horizon, left_road, right_road, middle_road
    for widget in window.winfo_children():
        widget.destroy()
    start_button.destroy()
    help_button.destroy()
    load_file_button.destroy()
    state = "help"

    help_title = tk.Label(window, bg='#235937', text="Help", font=('', 12, 'bold'), fg='#FFE86E')
    window.create_window(250, 20, anchor='center', window=help_title)

    s_text = "The program starts on the settings page where you should\n" \
             "enter an email address, the speed limit, and the location\n" \
             "of the Traffic Camera. Clicking the \"Start\" button\n" \
             "should close the settings options and begin displaying\n" \
             "the video feed if all entries have been entered correctly.\n" \
             "Please set up the Traffic Camera according to the image\n" \
             "below or use pre-recorded videos of the same format."
    start_text = tk.Label(window, bg='#235937', text=s_text, font=('', 12), fg='#FFFFFF')
    window.create_window(250, 35, anchor='n', window=start_text)

    border = window.create_rectangle(180, 175, 320, 255, fill='#FFFFFF')
    horizon = window.create_line(180, 215, 320, 215)
    left_road = window.create_line(200, 215, 240, 255)
    right_road = window.create_line(215, 215, 320, 235)
    middle_road = window.create_line(207, 215, 305, 255, dash=5)

    how_it_works_text = "When a vehicle enters the frame, it should be detected\n" \
                        "and its speed should be measured. The vehicle's\n" \
                        "measured speed is then compared with the speed limit\n" \
                        "entered on the settings page. If the speed limit is\n" \
                        "exceeded, an email is sent to the email address entered\n" \
                        "on the settings page. The email will include the time\n" \
                        "of the violation, the location entered on the settings\n" \
                        "page, the measured speed, a picture of the vehicle, as\n" \
                        "well as a video. For more information please visit the\n" \
                        "GitHub page by clicking \"GitHub\" below."
    settings_label = tk.Label(window, bg='#235937', text=how_it_works_text, font=('', 12), fg='#FFFFFF')
    window.create_window(250, 260, anchor='n', window=settings_label)

    back_button = tk.Button(text="Back", width=10, font=('', 12), command=settings)
    window.create_window(230, 470, anchor='e', window=back_button)

    github_button = tk.Button(text="GitHub", width=10, font=('', 12), command=lambda:webbrowser.open_new("https://github.com/ogarbanz/CSC380-TrafficCamera"))
    window.create_window(270, 470, anchor='w', window=github_button)


def start_stream():
    global user_email, user_speed, user_location, email_field, speed_field, location_field
    user_email = email_field.get()
    user_speed = speed_field.get()
    user_location = location_field.get()

    regex = '^(\w|\.|\_|\-)+[@](\w|\_|\-|\.)+[.]\w{2,3}$'
    if (user_email == "") | (user_speed == "") | (user_location == ""):
        tk.messagebox.showerror(title="Error", message="Invalid entry")
    elif (not re.search(regex, user_email)) | (not user_speed.isdigit()) | (len(user_location) > 85):
        tk.messagebox.showerror(title="Error", message="Invalid entry")
    elif (int(user_speed) < 0) | (int(user_speed) > 60):
        tk.messagebox.showerror(title="Error", message="Invalid entry")
    elif not os.path.exists("haarcascade_car.xml"):
        tk.messagebox.showerror(title="Error", message="Cannot find haarcascade_car.xml")
        exit(1)
    else:
        root.destroy()
        cv.start_stream(file, user_email, user_speed, user_location)


def start_ui():
    global root, window, state, file
    file = None

    root = tk.Tk()
    root.title("Traffic Camera")
    root.resizable(False, False)

    window = tk.Canvas(root, width=500, height=500)
    window.configure(bg='#235937')
    window.pack()
    state = "settings"
    settings()
    root.mainloop()


if __name__ == "__main__":
    start_ui()
