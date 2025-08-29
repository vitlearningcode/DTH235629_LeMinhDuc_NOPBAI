#hàm
a = int(input('Nhập a: ')) 
b = int(input('Nhập b: ')) 
def TinhTong(a,b): return a + b 
tong = TinhTong(a,b) 
print(tong)

print('----------------------------------------------------------------------------\n')

def xep_loai(diem_cua_hoc_sinh, diem_chuan=5.0): 
    if diem_cua_hoc_sinh >= diem_chuan: 
        return 'Tốt nghiệp' 
    else: 
        return 'Chưa tốt nghiệp' 

def printme(str): 
    print(str) 
    return 
printme(str = 'Hello Python') 

def TinhChuViDienTich(dai,rong): 
    chu_vi = (dai + rong)*2 
    dien_tich = (dai*rong) 
    return chu_vi, dien_tich 

#phạm vi biến
'''
def vi_du(): 
    x = 'Biến cục bộ' 
# Gọi hàm 
vi_du() 
print(x) 

--> NameError: name 'x' is not defined 
'''

x = 'Biến toàn cục' 
def vi_du(): 
    global x 
    print('Sử dụng x trong hàm vi_du()', x) 
# Gọi hàm 
vi_du() 
print('Sử dụng x ngoài hàm vi_du()', x) 


#hàm vô danh
binh_phuong = lambda x:x*x 
print(binh_phuong(2))

