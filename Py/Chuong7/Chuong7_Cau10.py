import json
import os

class Student:
    def __init__(self, ma, ten, namsinh, malop):
        self.ma = ma
        self.ten = ten
        self.namsinh = int(namsinh)
        self.malop = malop

class StudentManager:
    def __init__(self, file_path="sinhvien.json"):
        self.file_path = file_path
        self.students = []
        self.load_data()

    def load_data(self):
        if os.path.exists(self.file_path):
            with open(self.file_path, "r", encoding="utf-8") as f:
                data = json.load(f)
                self.students = [Student(**sv) for sv in data]

    def save_data(self):
        with open(self.file_path, "w", encoding="utf-8") as f:
            json.dump([vars(sv) for sv in self.students], f, ensure_ascii=False, indent=4)

    def add_student(self, sv):
        self.students.append(sv)
        self.save_data()

    def update_student(self, ma, ten=None, namsinh=None, malop=None):
        for sv in self.students:
            if sv.ma == ma:
                if ten: sv.ten = ten
                if namsinh: sv.namsinh = int(namsinh)
                if malop: sv.malop = malop
                self.save_data()
                return True
        return False

    def delete_student(self, ma):
        self.students = [sv for sv in self.students if sv.ma != ma]
        self.save_data()

    def search(self, keyword):
        return [sv for sv in self.students if keyword.lower() in sv.ten.lower()]

    def sort_by_year(self):
        self.students.sort(key=lambda sv: sv.namsinh)
        self.save_data()

# --- Demo ---
if __name__ == "__main__":
    manager = StudentManager()

    # Thêm dữ liệu mẫu
    manager.add_student(Student("SV01", "Nguyen Van A", 2002, "CT01"))
    manager.add_student(Student("SV02", "Tran Thi B", 2003, "CT02"))

    print("Danh sách sinh viên:")
    for sv in manager.students:
        print(f"{sv.ma} - {sv.ten} - {sv.namsinh} - {sv.malop}")

    print("\nTìm 'Nguyen':", [sv.ten for sv in manager.search("Nguyen")])