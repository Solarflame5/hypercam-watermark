import tkinter as tk

root = tk.Tk()
root.geometry('168x16+0+0')
root.resizable(False, False)
root.attributes('-topmost', 1)
root.overrideredirect(True)

text = tk.Label(root, text = "Unregistered Hypercam 2", bd = 0, font = "System")
text.pack()
root.mainloop()