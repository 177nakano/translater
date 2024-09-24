import tkinter as tk
import main
import time

class App(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack() #selfがframeになる 。
        
        self.text = "ここにテキストが入ります"

        self.frame = tk.Frame(self,pady=10,padx=5,relief=tk.GROOVE,width=350,height=350)
        self.frame.pack()

        self.label = tk.Label(self.frame,text=self.text,wraplength=300)
        self.label.pack(anchor="center")

        buttom = tk.Button(text="Translate",command=self.delay)
        buttom.place(relx=0.5,rely=0.9,anchor=tk.CENTER)

    def delay(self):
        self.label.configure(text="翻訳する範囲を選択してください")

        self.after(1,self.change_text)

    def change_text(self):
        #text = "change"

        text = main.translate()
        if text:
            self.label.configure(text=text)
        else:
            self.label.configure(text="翻訳結果が得られませんでした。")
