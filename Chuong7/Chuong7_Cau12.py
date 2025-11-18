import csv
import random

FILE_PATH = "dulieu.csv"

def tao_file_csv():
    with open(FILE_PATH, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f, delimiter=';')
        for _ in range(10):  # 10 dòng
            row = [random.randint(0, 100) for _ in range(10)]  # 10 số
            writer.writerow(row)
    print(f"Đã tạo file CSV '{FILE_PATH}' thành công!")

def doc_va_tinh_tong():
    with open(FILE_PATH, "r", encoding="utf-8") as f:
        reader = csv.reader(f, delimiter=';')
        print("\nTổng giá trị mỗi dòng trong file CSV:\n")
        for i, row in enumerate(reader, start=1):
            numbers = [int(x) for x in row if x.strip() != ""]
            tong = sum(numbers)
            print(f"Dòng {i}: {numbers} ➜ Tổng = {tong}")

if __name__ == "__main__":
    tao_file_csv()
    doc_va_tinh_tong()