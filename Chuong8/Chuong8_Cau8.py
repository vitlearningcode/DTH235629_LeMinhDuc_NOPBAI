from tkinter import *

root = Tk()
root.title("Chuyển độ F sang độ C")

root.configure(bg="yellow")

do_F = StringVar()
do_C = StringVar()

def chuyen_doi():
    try:
        f = float(do_F.get())
        c = (f - 32) * 5 / 9
        do_C.set(f"{c:.2f}")
    except:
        do_C.set("Lỗi nhập!")

frame = Frame(root, bg="yellow", bd=2, relief="solid", padx=10, pady=10)
frame.pack(padx=20, pady=20)

Label(frame, text="Nhập độ F", bg="yellow", font=("Arial", 12)).grid(row=0, column=0, padx=5, pady=5)
Entry(frame, textvariable=do_F, width=10, fg="red", font=("Arial", 12)).grid(row=0, column=1, padx=5, pady=5)

Button(frame, text="Chuyển", bg="lightblue", font=("Arial", 11, "bold"), command=chuyen_doi).grid(row=1, column=1, pady=5)

Label(frame, text="Độ C", bg="yellow", font=("Arial", 12)).grid(row=2, column=0, padx=5, pady=5)
Entry(frame, textvariable=do_C, width=15, font=("Arial", 12), state="readonly").grid(row=2, column=1, padx=5, pady=5)

root.mainloop()