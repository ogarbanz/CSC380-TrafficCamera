import tkinter as tk

root = tk.Tk()
root.title("Settings")
root.iconbitmap('car_icon.ico')

width, height = root.winfo_screenwidth() / 3, root.winfo_screenheight() / 2
root = tk.Canvas(root, width=width, height=height)
root.configure(bg='#235937')
root.pack()

if __name__ == '__main__':

    settings_title = tk.Label(root,bg='#235937', text="Settings", font=('', 20, 'bold'), fg='#FFFFFF')
    root.create_window(width / 2, height / 12, anchor='center', window=settings_title)

    email_field = tk.Entry(root, width=30, bd=3)
    root.create_window(width / 2, height / 4, anchor='e', window=email_field)

    email_save = tk.Button(text='SAVE', width=10, height=1, font=('', 12))
    root.create_window(width / 2 + 75, height / 4, anchor='w', window=email_save)

    speed_field = tk.Entry(root, width=30, bd=3)
    root.create_window(width / 2, height / 4 + 50, anchor='e', window=speed_field)

    speed_save = tk.Button(text='SAVE', width=10, height=1, font=('', 12))
    root.create_window(width / 2 + 75, height / 4 + 50, anchor='w', window=speed_save)

    local_field = tk.Entry(root, width=30, bd=3)
    root.create_window(width / 2, height / 4 + 100, anchor='e', window=local_field)

    local_save = tk.Button(text='SAVE', width=10, height=1, font=('', 12))
    root.create_window(width / 2 + 75, height / 4 + 100, anchor='w', window=local_save)

    back_button = tk.Button(text='BACK', width=10, height=1, font=('',12))
    root.create_window(width / 2, height / 2 + 150, anchor='center', window=back_button)

    root.mainloop()
