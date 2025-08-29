'''
Ví dụ kiểu số nguyên trong Python
'''

# Khai báo và gán giá trị số nguyên bằng 49 cho biến siso 
siso = 40 

# Hiển thị giá trị biến siso ra màn hình 
print('Sĩ số lớp = ',siso) 

# Hiển thị kiểu dữ liệu của biến siso 
print(type(siso)) 

'''
Ví dụ kiểu số thực trong 
Python: float
'''
print('---------------------\n')
  
# Khai báo và gán giá trị số thực bằng 6.5 cho biến điemtoan 
diemtoan = 6.5 
# Hiển thị giá trị biến điemtoan ra màn hình 
print('Điểm thi = ',diemtoan) 
# Hiển thị kiểu dữ liệu của biến điemtoan 
print(type(diemtoan)) 

'''
Chương trình minh họa hàm type và 3 kiểu dữ liệu cơ bản
trong Python: int, float, str, bool
'''
str = 'Trường Đại học An Giang' 
n = 100 
HeSoLuong = 2.34 
print('Kiểu dữ liệu của biến str là ', type(str)) 
print('Kiểu dữ liệu của biến n là ', type(n)) 
print('Kiểu dữ liệu của biến HeSoLuong là ', type(HeSoLuong)) 
print('Kiểu dữ liệu của phép toán so sánh 1 > 0 là', type(1>0))

# Khai báo hằng số PI
PI = 3.14159 

'''
 Chương trình bị lỗi khi vi phạm nguyên tắc sử dụng biến 
 '''
 
'''
    s = ’5’ 
    s = s + 15 
    print(s) 
    
    Lỗi: TypeError: can only concatenate str (not "int") to str    
 '''
print('---------------------\n')
 # Sửa lỗi bằng cách ép kiểu
s = '5'
s = int(s) + 15 
print(s) 


 
 