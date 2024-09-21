import tkinter as tk
import main

class App(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack() #selfがframeになる 。
        
        self.text = "ここにテキストが入ります"

        self.label = tk.Label(self,text=self.text,wraplength=300)
        self.label.pack(anchor="center")

        buttom = tk.Button(text="Exit",command=self.change_text)
        buttom.place(relx=0.5,rely=0.9,anchor=tk.CENTER)

    def change_text(self):
        #text = "change"
        text = main.translate()

        self.label.configure(text=text)
