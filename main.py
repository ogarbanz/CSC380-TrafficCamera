import tkinter as tk
import tkinter.messagebox
import re
import cv


def settings():
    global state, start_button, help_button, email_field, speed_field, location_field

    for widget in window.winfo_children():
        widget.destroy()
    if state == "help":
        back_button.destroy()
    state = "settings"

    settings_title = tk.Label(window, bg='#235937', text="Settings", font=('', 12, 'bold'), fg='#FFE86E')
    window.create_window(250, 20, anchor='center', window=settings_title)

    email_label = tk.Label(window, bg='#235937', text="Email", font=('', 12), fg='#FFFFFF')
    window.create_window(150, 80, anchor='e', window=email_label)
    email_field = tk.Entry(window, width=30, bd=3)
    window.create_window(250, 80, anchor='center', window=email_field)

    speed_label = tk.Label(window, bg='#235937', text="Speed Limit", font=('', 12), fg='#FFFFFF')
    window.create_window(150, 120, anchor='e', window=speed_label)
    speed_field = tk.Entry(window, width=30, bd=3)
    window.create_window(250, 120, anchor='center', window=speed_field)

    location_label = tk.Label(window, bg='#235937', text="Location", font=('', 12), fg='#FFFFFF')
    window.create_window(150, 160, anchor='e', window=location_label)
    location_field = tk.Entry(window, width=30, bd=3)
    window.create_window(250, 160, anchor='center', window=location_field)

    start_button = tk.Button(text="Start", width=10, font=('', 12), command=start_stream)
    window.create_window(230, 240, anchor='e', window=start_button)

    help_button = tk.Button(text="Help", width=10, font=('', 12), command=help)
    window.create_window(270, 240, anchor='w', window=help_button)


def help():
    global state, back_button
    for widget in window.winfo_children():
        widget.destroy()
    start_button.destroy()
    help_button.destroy()
    state = "help"

    help_title = tk.Label(window, bg='#235937', text="Help", font=('', 12, 'bold'), fg='#FFE86E')
    window.create_window(250, 20, anchor='center', window=help_title)

    getting_started = tk.Label(window, bg='#235937', text="Getting Started", font=('', 12, 'italic'), fg='#FFFFFF')
    window.create_window(250, 60, anchor='center', window=getting_started)

    s_text = """Upon starting the program, you will be greeted by the
        settings page of the Traffic Camera software. Here, you can
        modify the destination of the email notification, the speed limit,
        and the location of the camera. At the bottom of the screen are
        two buttons. The 'Start' button saves all of the fields entered
        and starts the video stream. The 'Help' button takes you to 
        this help page."""
    start_text = tk.Label(window, bg='#235937', text=s_text, font=('', 12), fg='#FFFFFF')
    window.create_window(250, 80, anchor='n', window=start_text)

    how_it_works_title = tk.Label(window, bg='#235937', text="How It Works", font=('', 12, 'italic'), fg='#FFFFFF')
    window.create_window(250, 240, anchor='center', window=how_it_works_title)

    how_it_works_text = """Each time a vehicle enters the frame, its speed
        is measured. When a vehicle's measured speed exceeds
        the speed limit, an email notification will be sent."""
    settings_label = tk.Label(window, bg='#235937', text=how_it_works_text, font=('', 12), fg='#FFFFFF')
    window.create_window(250, 260, anchor='n', window=settings_label)

    back_button = tk.Button(text="Back", width=10, font=('', 12), command=settings)
    window.create_window(250, 360, anchor='center', window=back_button)


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
        cv.start_stream()


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
