'''
Ví dụ: Chương trình hoán vị giá trị cho 2 biến x, y.Với các ngôn 
ngữ lập trình truyền thống cần ít nhất một biến nhớ tạm để thực hiện.
'''
x, y = 3, 5 
tmp = x 
x = y 
y = tmp 

print("x =", x, ", y =", y) # x = 5 , y = 3

x,y = y,x 
print("x =", x, ", y =", y) # x = 3 , y = 5