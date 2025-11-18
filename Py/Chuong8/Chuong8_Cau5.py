import tkinter as tk

def tao_giao_dien_don_gian():
    # 1. Khởi tạo cửa sổ chính
    root = tk.Tk()
    root.title("Enter New Password")
    root.resizable(False, False) # Giữ cố định kích thước

    # --- 2. Tạo Label và Entry cho 3 hàng nhập liệu ---

    # Hàng 0: Old Password
    tk.Label(root, text="Old Password:", width=22, anchor="w").grid(row=0, column=0, padx=5, pady=5, sticky="w")
    tk.Entry(root, width=30, show='*').grid(row=0, column=1, padx=5, pady=5, sticky="we")

    # Hàng 1: New Password
    tk.Label(root, text="New Password:", width=22, anchor="w").grid(row=1, column=0, padx=5, pady=5, sticky="w")
    tk.Entry(root, width=30, show='*').grid(row=1, column=1, padx=5, pady=5, sticky="we")

    # Hàng 2: Enter New Password Again
    tk.Label(root, text="Enter New Password Again:", width=22, anchor="w").grid(row=2, column=0, padx=5, pady=5, sticky="w")
    tk.Entry(root, width=30, show='*').grid(row=2, column=1, padx=5, pady=5, sticky="we")

    # --- 3. Tạo và sắp xếp các Nút (Button) ---

    # Tạo 2 nút OK và Cancel
    btn_ok = tk.Button(root, text="OK", width=8, command=lambda: print("OK clicked"))
    btn_cancel = tk.Button(root, text="Cancel", width=8, command=root.quit) # root.destroy đóng cửa sổ

    # Đặt các nút ở Hàng 3. Sử dụng columnspan=2 để chúng nằm dưới cả 2 cột.
    # Sử dụng sticky="e" để căn các nút sang phải.
    btn_ok.grid(row=3, column=0, padx=5, pady=10, sticky="e")
    btn_cancel.grid(row=3, column=1, padx=5, pady=10, sticky="w")
    
    # ⚠️ Lưu ý: Trong cách bố trí này, chỉ cần sticky cho từng nút thay vì dùng Frame chứa.

    # 4. Cho Cột 1 co giãn (để Entry co giãn theo)
    root.grid_columnconfigure(1, weight=1)

    # 5. Chạy giao diện
    root.mainloop()

if __name__ == '__main__':
    tao_giao_dien_don_gian()