import tkinter as tk
import tkinter.messagebox
import webbrowser
import re
import cv


def settings():
    global state, start_button, help_button, email_field, speed_field, location_field

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


def help():
    global state, back_button, github_button, border, horizon, left_road, right_road, middle_road
    for widget in window.winfo_children():
        widget.destroy()
    start_button.destroy()
    help_button.destroy()
    state = "help"

    help_title = tk.Label(window, bg='#235937', text="Help", font=('', 12, 'bold'), fg='#FFE86E')
    window.create_window(250, 20, anchor='center', window=help_title)

    s_text = "The program starts on the settings page where you should enter an\n" \
             "email address, the speed limit, and the location of the Traffic\n" \
             "Camera. Clicking the \"Start\" button should close the settings\n" \
             "options and begin displaying the video feed if all entries have\n" \
             "been entered correctly. Clicking the \"Help\" button will bring\n" \
             "you to this page. Please set up the Traffic Camera according to\n" \
             "the image below."
    start_text = tk.Label(window, bg='#235937', text=s_text, font=('', 12), fg='#FFFFFF')
    window.create_window(250, 35, anchor='n', window=start_text)

    border = window.create_rectangle(180, 175, 320, 255, fill='#FFFFFF')
    horizon = window.create_line(180, 215, 320, 215)
    left_road = window.create_line(200, 215, 240, 255)
    right_road = window.create_line(215, 215, 320, 235)
    middle_road = window.create_line(207, 215, 305, 255, dash=5)

    how_it_works_text = "When a vehicle enters the frame, it should be detected and its\n" \
                        "speed should be measured. The vehicle's measured speed is then\n" \
                        "compared with the speed limit entered on the settings page. If\n" \
                        "the speed limit is exceeded, an email is sent to the email address\n" \
                        "entered on the settings page. The email will include the time of\n" \
                        "the violation, the location entered on the settings page, the\n" \
                        "measured speed, and a picture of the vehicle.\n\n" \
                        "For more information please visit the GitHub page by clicking the\n" \
                        "\"GitHub\" button below."
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
    else:
        root.destroy()
        cv.start_stream(user_email, user_speed, user_location)


def start_ui():
    global root, window, state

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
