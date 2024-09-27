import tkinter as tk
from tkinter import ttk

"""def output_text(text):
    window = tk.Tk()
    window.title("TextOutptter")
    window.geometry("400x400+1520+580")
    window.attributes("-alpha",0.7)
    window.attributes("-topmost",True)

    frame = tk.Frame(window,pady=10,padx=5,relief=tk.GROOVE,width=350,height=350)
    frame.pack()

    label = tk.Label(frame,text=text,wraplength=300)
    label.pack(anchor="center")

    buttom = tk.Button(text="Exit",command=window.destroy)
    buttom.place(relx=0.5,rely=0.9,anchor=tk.CENTER)

    window.mainloop()"""

class Application(tk.Frame):
    def __init__(self,master):
        self.master.title("TextOutptter")
        self.master.geometry("400x400+1520+580")
        self.master.attributes("-alpha",0.7)
        self.master.attributes("-topmost",True)

        self.text = "ここに翻訳文が入ります"

        self.frame = tk.Frame(self.master,pady=10,padx=5,relief=tk.GROOVE,width=350,height=350)
        self.frame.pack()

        self.label = tk.Label(self.frame,text=self.text,wraplength=300)
        self.label.pack(anchor="center")


