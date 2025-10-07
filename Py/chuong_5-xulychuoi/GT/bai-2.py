'''Bài 2: Nhập vào 1 chuỗi, in ra chiều dài, ký tự đầu, cuối và chuỗi con từ vị trí i đến j.'''
s = input("nhap vao mot chuoi: ")
i = input("nhap vao chi so bat dau: ")
j = input('nhap vao chi so ket thuc')

print (f'chieu dai chuoi cua len:  {len(s)}')

if len (s) > 0:  
    print (f'ky tu dau tien : {s[0]}')
    print (f'ki tu cuoi cung : {S[-1]}')

if   0 <= i <= j  < len(s):
    print (f"cac ki tu tu vi tri {i} den {j} '{s[i:j + 1]}'")
else:
    print("Chỉ số i, j không hợp lệ!")
