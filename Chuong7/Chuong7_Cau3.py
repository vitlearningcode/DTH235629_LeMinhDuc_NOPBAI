from xml.dom.minidom import parse
import xml.dom.minidom
# Mở file xml bằng minidom parser
DOMTree = xml.dom.minidom.parse("employees.xml")
collection = DOMTree.documentElement
# Lấy tất cả tag là employee
employees = collection.getElementsByTagName("employee")
# Duyệt vòng lặp để lấy toàn bộ dữ liệu ra
for employee in employees:
    tag_id = employee.getElementsByTagName('id')[0]
    id=tag_id.childNodes[0].data
    tag_name = employee.getElementsByTagName('name')[0]
    name=tag_name.childNodes[0].data
    print(id,'\t',name)
#giải thích đoạn code trên
# Bước 1: Import thư viện xml.dom.minidom để làm việc với file XML.
# Bước 2: Sử dụng hàm parse() để mở và phân tích cú pháp của file XML có tên "employees.xml".
# Bước 3: Lấy phần tử gốc (root element) của tài liệu XML bằng thuộc tính documentElement.
# Bước 4: Sử dụng phương thức getElementsByTagName() để lấy tất cả các phần tử con có tên là "employee" và lưu chúng vào biến employees.
# Bước 5: Duyệt qua từng phần tử employee trong danh sách employees.    