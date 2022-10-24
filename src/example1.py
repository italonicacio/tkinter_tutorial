import tkinter as tk
from turtle import width

from setuptools import Command

class Person(tk.Frame):
    def __init__(self, name="Person"):
        tk.Frame.__init__(self)
        self.pack()
        self.master.title(name)
        self.button1 = tk.Button(self, text="Click Here", width=25, command=self.new_window)
        self.button1.grid(row=0, column=1, columnspan=2, sticky=tk.W+tk.E+tk.N+tk.S)
    
    def new_window(self):
        self.new_window_ = Person2()
    

class Person2(tk.Frame):
    def __init__(self, name="Person2"):
        new = tk.Frame.__init__(self)
        new = tk.Toplevel(self)
        new.title(name + " More Window")
        new.button = tk.Button(text = "Press to Close", width=25, command=self.close_window)

        new.button.pack()

    def close_window(self):
        self.destroy()


def main():
    Person().mainloop()

if __name__ == '__main__':
    main()