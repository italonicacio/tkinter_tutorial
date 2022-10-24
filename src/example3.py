import tkinter as tk

top = tk.Tk()

top.geometry("200x200")

spin = tk.Spinbox(top, from_=0, to=25)

spin.pack()

top.mainloop()