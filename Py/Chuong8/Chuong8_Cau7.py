from tkinter import *

root = Tk()
root.title("Chuyển năm Dương lịch sang Âm lịch")

root.configure(bg="yellow")

can = ["Canh", "Tân", "Nhâm", "Quý", "Giáp", "Ất", "Bính", "Đinh", "Mậu", "Kỷ"]
chi = ["Thân", "Dậu", "Tuất", "Hợi", "Tý", "Sửu", "Dần", "Mão", "Thìn", "Tỵ", "Ngọ", "Mùi"]

nam_duong = StringVar()
nam_am = StringVar()

def chuyen_doi():
    try:
        nam = int(nam_duong.get())
        can_index = nam % 10
        chi_index = nam % 12
        nam_am.set(can[can_index] + " " + chi[chi_index])
    except:
        nam_am.set("Lỗi nhập năm!")

Label(root, text="Nhập năm dương:", bg="yellow", font=("Arial", 12)).grid(row=0, column=0, padx=10, pady=10, sticky="e")
Entry(root, textvariable=nam_duong, width=10, fg="red", font=("Arial", 12)).grid(row=0, column=1, padx=10, pady=10)

Button(root, text="Chuyển", command=chuyen_doi, bg="lightblue", font=("Arial", 10)).grid(row=1, column=1, pady=5)

Label(root, text="Năm âm:", bg="yellow", font=("Arial", 12)).grid(row=2, column=0, padx=10, pady=10, sticky="e")
Entry(root, textvariable=nam_am, width=15, font=("Arial", 12), state="readonly").grid(row=2, column=1, padx=10, pady=10)

root.mainloop()