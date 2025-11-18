from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("Phần mềm tính BMI")
root.configure(bg="yellow")

chieucao = StringVar()
cannang = StringVar()
bmi_value = StringVar()
tinhtrang = StringVar()
nguyco = StringVar()

def tinh_BMI():
    try:
        cao = float(chieucao.get())
        nang = float(cannang.get())
        bmi = nang / (cao ** 2)
        bmi_value.set(f"{bmi:.2f}")
        
        if bmi < 18.5:
            tinhtrang.set("Gầy")
            nguyco.set("Thấp")
        elif bmi < 25:
            tinhtrang.set("Bình thường")
            nguyco.set("Trung bình")
        elif bmi < 30:
            tinhtrang.set("Hơi béo")
            nguyco.set("Hơi cao")
        else:
            tinhtrang.set("Béo phì")
            nguyco.set("Rất cao")
    except:
        messagebox.showerror("Lỗi", "Vui lòng nhập đúng số!")

def thoat():
    root.destroy()

frame = Frame(root, bg="yellow", bd=2, relief="solid", padx=15, pady=15)
frame.pack(padx=20, pady=20)

Label(frame, text="Nhập chiều cao:", bg="yellow", font=("Arial", 11)).grid(row=0, column=0, sticky="e", pady=3)
Entry(frame, textvariable=chieucao, width=10, fg="red", font=("Arial", 12)).grid(row=0, column=1, pady=3)

Label(frame, text="Nhập cân nặng:", bg="yellow", font=("Arial", 11)).grid(row=1, column=0, sticky="e", pady=3)
Entry(frame, textvariable=cannang, width=10, fg="red", font=("Arial", 12)).grid(row=1, column=1, pady=3)

Button(frame, text="Tính BMI", bg="lightblue", font=("Arial", 11, "bold"), command=tinh_BMI).grid(row=2, column=1, pady=6)

Label(frame, text="BMI của bạn:", bg="yellow", font=("Arial", 11)).grid(row=3, column=0, sticky="e", pady=3)
Entry(frame, textvariable=bmi_value, width=10, font=("Arial", 12), state="readonly").grid(row=3, column=1, pady=3)

Label(frame, text="Tình trạng của bạn:", bg="yellow", font=("Arial", 11)).grid(row=4, column=0, sticky="e", pady=3)
Entry(frame, textvariable=tinhtrang, width=15, font=("Arial", 12), state="readonly").grid(row=4, column=1, pady=3)

Label(frame, text="Nguy cơ phát triển bệnh:", bg="yellow", font=("Arial", 11)).grid(row=5, column=0, sticky="e", pady=3)
Entry(frame, textvariable=nguyco, width=15, font=("Arial", 12), state="readonly").grid(row=5, column=1, pady=3)

Button(frame, text="Thoát", bg="lightblue", font=("Arial", 11, "bold"), command=thoat).grid(row=6, column=1, pady=8)

root.mainloop()