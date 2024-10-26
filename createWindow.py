import tkinter as tk
import main



class App(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack() 
        
        self.text = "ここにテキストが入ります"

        self.frame = tk.Frame(self,pady=10,padx=5,relief=tk.GROOVE,width=350,height=350)
        self.frame.pack(fill=tk.BOTH, expand=True)

        self.label = tk.Label(self.frame,text=self.text,wraplength=300, justify="center")
        self.label.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        translate_buttom = tk.Button(text="Translate",command=self.delay)
        translate_buttom.place(relx=0.35,rely=0.9,anchor=tk.CENTER)

        elaboration_button = tk.Button(text="regeneration",command=self.elaboration)
        elaboration_button.place(relx=0.65,rely=0.9,anchor=tk.CENTER)

    def delay(self):
        self.label.configure(text="翻訳する範囲を選択してください")
        self.label.update_idletasks()

        self.after(1,self.change_text)

    def change_text(self):
        #text = "change"

        try:
            text = main.translate()
            self.label.configure(text=text)
        except Exception as e:
            self.label.configure(text=f"翻訳結果が得られませんでした。\n {e}")

    def elaboration(self):
        text = main.elaboration()
        self.label.configure(text=text)

        self.label.update_idletasks()
