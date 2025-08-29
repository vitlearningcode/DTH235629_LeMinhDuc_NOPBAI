#Cấu trúc lệnh vòng lặp 
# for 
for c in 'Python': 
    print(c, end='-') 
    
print('\n-----------------------\n')
    
n = int(input('Nhập số n: ')) 
s = 0 
for i in range(1,n): 
    if n % i == 0:  
        s = s + i 
if s == n: 
    print(n, ' là số hoàn hảo') 
else: 
    print(n, ' không là số hoàn hảo') 
    
    print('-----------------------\n')
    
n = int(input('Nhập n:')) 
for x in range(1,n,1): 
    if x % 2 == 0: 
        continue 
    print('x = ', x, ' là số lẻ')
    
#while
print('\n-----------------------\n')

a = int(input('Nhập số nguyên a: ')) 
b = int(input('Nhập số nguyên b: ')) 
while a != b: 
    if a > b: 
        a = a - b 
    else: 
        b = b - a 
print('Ước số chung lớn nhất của a và b là ', a)

print('\n-----------------------\n')

n = int(input('Nhập số n: ')) 
i = 1 
while True: 
    if i > n: 
        break 
    print(i) 
    i = i + 1 

print('\n-----------------------\n')

#tìm số tự nhiên n nhỏ nhất sao cho 1/n nhỏ hơn số thực a nhập từ bàn phím.
#Cách 1: 
a = float(input('Nhập số a: ')) 
n = 1 
while True: 
    if (1/n) < a: 
        break 
    n = n + 1 
print('Số n cần tìm là : ', n) 

print('\n-----------------------\n')
#Cách 2: 
a = float(input('Nhập số a: ')) 
n = 1 
while (1/n) < a: 
    break 
n = n + 1 
print('Số n cần tìm là : ', n) 

# Lệnh break và continue

a = 10 #Khai báo và khởi tạo biển nguyên a bằng 19 
while (a > 0):  #Khi biến a còn lớn hơn không thì thực hiện 
    a = a - 1 #Giảm a đi 1 đơn vị 
    if (a == 5):  #nếu a đúng bằng 5 
        continue #Quay lên đầu cấu trúc lặp, kiểm tra điều kiện a 
    print('Giá trị biến hiện tại là: ', a) 
print('Kết thúc...')

for i in 'ngôn ngữ lập trình Python': 
  print(i) #Hiển thị ký tự ra màn hình 
  if (i == 'g'): #Kiểm tra xem ký tự đọc được có bằng 'n'? 
    break #nếu đúng, thoát ra ngoài cấu trúc for ngay 
print('Kết thúc!') 