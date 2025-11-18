from tkinter import *

root = Tk()
root.title("frame 2")


reliefs = ["raised", "sunken", "flat", "ridge", "groove", "solid"]


for b in range(5):
    Label(root, text=f"borderwidth = {b}", width=15).grid(row=b, column=0, padx=5, pady=5)
    for j, r in enumerate(reliefs):
        Button(root, text=r, relief=r, borderwidth=b, width=10).grid(row=b, column=j+1, padx=3, pady=3)

root.mainloop()