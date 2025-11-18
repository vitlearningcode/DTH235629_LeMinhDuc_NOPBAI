import xml.etree.ElementTree as ET
from collections import defaultdict

# ----------- Đọc file XML -----------
def doc_nhom(file_nhom):
    tree = ET.parse(file_nhom)
    root = tree.getroot()
    ds_nhom = []
    for nhom in root.findall("nhom"):
        ma = nhom.find("ma").text
        ten = nhom.find("ten").text
        ds_nhom.append({"ma": ma, "ten": ten})
    return ds_nhom

def doc_thietbi(file_tb):
    tree = ET.parse(file_tb)
    root = tree.getroot()
    ds_tb = []
    for tb in root.findall("thietbi"):
        manhom = tb.get("manhom")
        ma = tb.find("ma").text
        ten = tb.find("ten").text
        ds_tb.append({"manhom": manhom, "ma": ma, "ten": ten})
    return ds_tb

# ----------- Hiển thị danh sách -----------
def hien_thi_nhom(ds_nhom):
    print("\nDANH SÁCH NHÓM THIẾT BỊ:")
    for n in ds_nhom:
        print(f"- {n['ma']}: {n['ten']}")

def hien_thi_thietbi(ds_tb):
    print("\nDANH SÁCH TOÀN BỘ THIẾT BỊ:")
    for tb in ds_tb:
        print(f"{tb['ma']:<5} | {tb['ten']:<15} | Nhóm: {tb['manhom']}")

# ----------- Lọc thiết bị theo nhóm -----------
def loc_theo_nhom(ds_tb, ma_nhom):
    kq = [tb for tb in ds_tb if tb["manhom"] == ma_nhom]
    return kq

# ----------- Nhóm có nhiều thiết bị nhất -----------
def nhom_nhieu_thietbi(ds_tb):
    dem = defaultdict(int)
    for tb in ds_tb:
        dem[tb["manhom"]] += 1
    nhom_max = max(dem, key=dem.get)
    return nhom_max, dem[nhom_max]

# ----------- Chương trình chính -----------
if __name__ == "__main__":
    file_nhom = "nhomthietbi.xml"
    file_tb = "thietbi.xml"

    ds_nhom = doc_nhom(file_nhom)
    ds_tb = doc_thietbi(file_tb)

    hien_thi_nhom(ds_nhom)
    hien_thi_thietbi(ds_tb)

    ma_nhom = input("\nNhập mã nhóm cần lọc (vd: n1): ").strip()
    kq = loc_theo_nhom(ds_tb, ma_nhom)
    print(f"\nThiết bị thuộc nhóm {ma_nhom}:")
    for tb in kq:
        print(f"  - {tb['ma']}: {tb['ten']}")

    manhom_max, so_luong = nhom_nhieu_thietbi(ds_tb)
    print(f"\nNhóm có nhiều thiết bị nhất: {manhom_max} ({so_luong} thiết bị)")