import tkinter as tk

root = tk.Tk()
root.title("Help")
root.iconbitmap('car_icon.ico')

scrollbar = tk.Scrollbar(root)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

width, height = root.winfo_screenwidth() / 3, root.winfo_screenheight() / 2
root = tk.Canvas(root, width=width, height=height)
root.configure(bg='#235937')
root.pack()

if __name__ == '__main__':

    help_title = tk.Label(root, bg='#235937', text="Help", font=('', 20, 'bold'), fg='#FFE86E')
    root.create_window(width / 2, height / 12, anchor='center', window=help_title)

    getting_started = tk.Label(root, bg='#235937', text="Getting Started", font=('', 15, "italic"), fg='#FFE86E')
    root.create_window(width / 2, height / 4, anchor='center', window=getting_started)

    s_text = """Upon starting the program, you will be greeted by the home
    page of the Traffic Camera software. Here, you can view the live feed 
    of the traffic camera, its location, its speed threshold, the infraction
    email destination, as well as the time and date. At the bottom of the 
    screen are two buttons which allow access to the settings page and the 
    help page."""
    start_text = tk.Label(root, bg='#235937', text=s_text, font=('', 10), fg='#FFFFFF')
    root.create_window(width / 2, height / 4 + 75, anchor='center', window=start_text)

    settings = tk.Label(root, bg='#235937', text="Settings", font=('', 15, "italic"), fg='#FFE86E')
    root.create_window(width / 2, height / 2 + 55, anchor='center', window=settings)

    settings_text = """Upon clicking the 'Settings' button on the home page, 
    a window will be presented giving you a couple options that allow
    modification. The first text box allows you to manipulate the current
    email that will be sent the infraction. The second text box allows you to 
    manipulate the speed threshold of the traffic camera. The third text box 
    allows you to manipulate the current location of the traffic camera. 
    Clicking on the 'SAVE' button next to these text boxes modifies the value
    of the respective text box. Once you are complete with the changes, 
    clicking on the back button will bring you back to the home page, where 
    the updated values will be displayed."""
    settings_par = tk.Label(root, bg='#235937', text=settings_text, font=('', 10), fg='#FFFFFF')
    root.create_window(width / 2, height / 2 + 160, anchor='center', window=settings_par)

    scrollbar.config(command=root.yview)

    root.mainloop()
