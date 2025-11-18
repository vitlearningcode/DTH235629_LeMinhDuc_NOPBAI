from tkinter import *

# Biến toàn cục để lưu trữ biểu thức toán học hiện tại
bieu_thuc = ""

# --- Các Hàm Xử Lý Sự Kiện ---

def nhap_ky_tu(ky_tu):
    """Xử lý khi người dùng nhấn số hoặc phép toán."""
    global bieu_thuc
    
    # Nối ký tự mới vào biểu thức hiện tại
    bieu_thuc = bieu_thuc + str(ky_tu)
    
    # Cập nhật ô hiển thị
    ket_qua_hien_thi.set(bieu_thuc)

def tinh_toan():
    """Xử lý khi người dùng nhấn nút '='."""
    global bieu_thuc
    try:
        # Sử dụng hàm eval() để tính giá trị của chuỗi biểu thức
        ket_qua = str(eval(bieu_thuc))
        
        # Hiển thị kết quả
        ket_qua_hien_thi.set(ket_qua)
        
        # Đặt lại biểu thức bằng kết quả vừa tính để tiếp tục phép tính
        bieu_thuc = ket_qua
        
    except ZeroDivisionError:
        # Xử lý lỗi chia cho 0
        ket_qua_hien_thi.set("Lỗi: Chia 0")
        bieu_thuc = ""
        
    except:
        # Xử lý các lỗi cú pháp khác (ví dụ: nhập '++')
        ket_qua_hien_thi.set("Lỗi cú pháp")
        bieu_thuc = ""

def xoa_tat_ca():
    """Xử lý khi người dùng nhấn nút 'Clr'."""
    global bieu_thuc
    bieu_thuc = ""
    ket_qua_hien_thi.set("")

# --- Khởi tạo Giao diện (GUI) ---

# 1. Tạo cửa sổ chính
root = Tk()
root.title("Máy Tính Đơn Giản")
# Đặt kích thước cố định và không cho thay đổi kích thước
root.geometry("260x350")
root.resizable(False, False)

# 2. Biến liên kết với ô hiển thị
ket_qua_hien_thi = StringVar()

# 3. Tạo ô hiển thị kết quả/biểu thức
o_hien_thi = Entry(root, textvariable=ket_qua_hien_thi, font=('Arial', 16), 
                   justify='right', bd=5, relief=SUNKEN)
o_hien_thi.grid(row=0, columnspan=4, sticky="nsew", ipadx=8, ipady=8)

# --- 4. Tạo các Nút và Đặt vào Lưới (Grid) ---

# Ghi chú: Sử dụng hàm lambda để truyền tham số (ký tự) vào hàm nhap_ky_tu
# padx và pady là khoảng đệm (padding) để nút trông đẹp hơn

# Hàng 1: Số 7, 8, 9 và Dấu cộng (+)
Button(root, text='7', command=lambda: nhap_ky_tu('7'), height=2, width=6).grid(row=1, column=0, padx=5, pady=5)
Button(root, text='8', command=lambda: nhap_ky_tu('8'), height=2, width=6).grid(row=1, column=1, padx=5, pady=5)
Button(root, text='9', command=lambda: nhap_ky_tu('9'), height=2, width=6).grid(row=1, column=2, padx=5, pady=5)
Button(root, text='+', command=lambda: nhap_ky_tu('+'), height=2, width=6, bg='lightblue').grid(row=1, column=3, padx=5, pady=5)

# Hàng 2: Số 4, 5, 6 và Dấu trừ (-)
Button(root, text='4', command=lambda: nhap_ky_tu('4'), height=2, width=6).grid(row=2, column=0, padx=5, pady=5)
Button(root, text='5', command=lambda: nhap_ky_tu('5'), height=2, width=6).grid(row=2, column=1, padx=5, pady=5)
Button(root, text='6', command=lambda: nhap_ky_tu('6'), height=2, width=6).grid(row=2, column=2, padx=5, pady=5)
Button(root, text='-', command=lambda: nhap_ky_tu('-'), height=2, width=6, bg='lightblue').grid(row=2, column=3, padx=5, pady=5)

# Hàng 3: Số 1, 2, 3 và Dấu nhân (*)
Button(root, text='1', command=lambda: nhap_ky_tu('1'), height=2, width=6).grid(row=3, column=0, padx=5, pady=5)
Button(root, text='2', command=lambda: nhap_ky_tu('2'), height=2, width=6).grid(row=3, column=1, padx=5, pady=5)
Button(root, text='3', command=lambda: nhap_ky_tu('3'), height=2, width=6).grid(row=3, column=2, padx=5, pady=5)
Button(root, text='*', command=lambda: nhap_ky_tu('*'), height=2, width=6, bg='lightblue').grid(row=3, column=3, padx=5, pady=5)

# Hàng 4: Dấu thập phân (.), Số 0, Dấu bằng (=) và Dấu chia (/)
Button(root, text='.', command=lambda: nhap_ky_tu('.'), height=2, width=6).grid(row=4, column=0, padx=5, pady=5)
Button(root, text='0', command=lambda: nhap_ky_tu('0'), height=2, width=6).grid(row=4, column=1, padx=5, pady=5)
Button(root, text='=', command=tinh_toan, height=2, width=6, bg='lightgreen').grid(row=4, column=2, padx=5, pady=5)
Button(root, text='/', command=lambda: nhap_ky_tu('/'), height=2, width=6, bg='lightblue').grid(row=4, column=3, padx=5, pady=5)

# Hàng 5: Nút Xóa (Clr) - Chiếm toàn bộ chiều rộng
Button(root, text='Clr', command=xoa_tat_ca, height=2, width=25, bg='red', fg='white').grid(row=5, column=0, columnspan=4, padx=5, pady=5, sticky="nsew")

# 5. Chạy vòng lặp chính
root.mainloop()