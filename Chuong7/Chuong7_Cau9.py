import os

class Category:
    def __init__(self, ma, ten):
        self.ma = ma
        self.ten = ten

class Product:
    def __init__(self, ma, ten, dongia, madm):
        self.ma = ma
        self.ten = ten
        self.dongia = float(dongia)
        self.madm = madm

class ProductManager:
    def __init__(self, file_path="sanpham.txt"):
        self.file_path = file_path
        self.products = []
        self.load_data()

    def load_data(self):
        if not os.path.exists(self.file_path):
            return
        with open(self.file_path, "r", encoding="utf-8") as f:
            for line in f:
                ma, ten, dongia, madm = line.strip().split("|")
                self.products.append(Product(ma, ten, dongia, madm))

    def save_data(self):
        with open(self.file_path, "w", encoding="utf-8") as f:
            for p in self.products:
                f.write(f"{p.ma}|{p.ten}|{p.dongia}|{p.madm}\n")

    def add_product(self, p):
        self.products.append(p)
        self.save_data()

    def update_product(self, ma, ten=None, dongia=None, madm=None):
        for p in self.products:
            if p.ma == ma:
                if ten: p.ten = ten
                if dongia: p.dongia = float(dongia)
                if madm: p.madm = madm
                self.save_data()
                return True
        return False

    def delete_product(self, ma):
        self.products = [p for p in self.products if p.ma != ma]
        self.save_data()

    def search(self, keyword):
        return [p for p in self.products if keyword.lower() in p.ten.lower()]

    def sort_by_price(self):
        self.products.sort(key=lambda x: x.dongia)
        self.save_data()

# --- Demo ---
if __name__ == "__main__":
    manager = ProductManager()

    # Thêm dữ liệu mẫu
    manager.add_product(Product("SP01", "Bút bi", 5000, "DM01"))
    manager.add_product(Product("SP02", "Vở kẻ ngang", 12000, "DM01"))

    print("Danh sách sản phẩm:")
    for p in manager.products:
        print(f"{p.ma} - {p.ten} - {p.dongia} - {p.madm}")

    print("\nTìm 'Bút':", [p.ten for p in manager.search("Bút")])