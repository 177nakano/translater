import tkinter as tk

def output_text(text):
    window = tk.Tk()
    window.title("TextOutptter")
    window.geometry("300x400+1000+100")

    label = tk.Label(text=text)
    label.pack()#.grid(column=0,row=0)
    buttom = tk.Button(text="Exit",command=window.destroy)
    buttom.pack()#.grid(column=0,row=1)

    window.mainloop()