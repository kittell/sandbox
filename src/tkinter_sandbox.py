'''
Created on Mar 21, 2020

@author: kirk@kirkkittell.com
'''

import tkinter as tk

def hello_world():
    # https://docs.python.org/3/library/tkinter.html#a-simple-hello-world-program
    
    class Application(tk.Frame):
        def __init__(self, master=None):
            super().__init__(master)
            self.master = master
            self.pack()
            self.create_widgets()
            
        def create_widgets(self):
            self.hi_there = tk.Button(self)
            self.hi_there["text"] = "Hello world\n(click me)"
            self.hi_there["command"] = self.say_hi
            self.hi_there.pack(side="top")
            
            self.quit = tk.Button(self, text="Quit", fg="red", command=self.master.destroy)
            self.quit.pack(side="bottom")
            
        def say_hi(self):
            print("hi there, everyone!")
            
    root = tk.Tk()
    app = Application(master=root)
    app.mainloop()
    

hello_world()