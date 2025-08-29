'''
Giả sử một người A có số tiền bằng X, đem gửi tiết kiệm với lãi 
suất tháng là 0,6%; hỏi rằng sau 18 tháng thì A có tất cả bao nhiêu 
tiền? Hãy viết chương trình cho người dùng nhập vào số tiền X sau 
đó tính tổng tiền sau 18 tháng. Biết rằng cứ 6 tháng thì tiền lãi được 
cộng vào gốc và người A không rút tiền. '''

#phân tích:
'''
 18 tháng = 3 kỳ lãi
 6 tháng cộng lãi 1 lần
 lãi suất 0.6% = 0.006
 tiền sau 1 tháng = gốc + gốc*lãi suất = gốc*(1 + lãi suất)
 tiền sau 6 tháng = gốc *(1 + lãi suất)^6
 tiền sau 18 tháng = gốc *(1 + lãi suất)^(6*3)
 '''
 
 #cơ bản
Goc = float (input("Nhập sốt tiền gốc: "))
LaiSuat = 0.006
Sum = Goc * (1 + LaiSuat)**18
print("Tổng tiền sau 18 tháng là: ", round(Sum,2))

#nâng cao
X = float (input ("Nhập sốt tiền gốc: "))
r = 0.006
months = 18
period = 6 #kỳ lãi

Tong = X
for i in range (months//period):
    Tong = Tong * (1 + r)**period
print ("Tổng tiền sau 18 tháng là: ", round(Tong,2))

#Tối ưu
def tinh_tong_tien(goc, lai_suat, thang, ky_lai):
    tong = goc
    for i in range (thang // ky_lai):
        tong *= (1 + lai_suat)**ky_lai
    return round(tong, 2)

X = float (input ("Nhập sốt tiền gốc: "))
r = 0.006
months = 18
period = 6 #kỳ lãi

Tong = tinh_tong_tien(X, r, months, period)
print ("Tổng tiền sau 18 tháng là: ", round(Tong,2))