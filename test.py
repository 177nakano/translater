import tkinter as tk

root = tk.Tk()
print(f"Tkinter version: {root.tk.call('info', 'patchlevel')}")
root.destroy()
