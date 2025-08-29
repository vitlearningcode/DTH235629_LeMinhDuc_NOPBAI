'''
Viết chương trình cho người dùng nhập vào từ bàn phím hai số a, b 
và một ký tự ch. Kiểm tra, nếu: ch là '+' thì thực hiện phép tính a + 
b và in kết quả lên màn hình, nếu ch là '_' thì thực hiện phép tính a - b và in kết quả lên màn hình, nếu ch là '*' thì thực hiện phép tính 
a * b và in kết quả lên màn hình, nếu ch là '/' thì thực hiện phép 
tính a / b và in kết quả lên màn hình, nếu ch là ký tự khác các ký tự 
trên thì hiển thị ra màn hình 'ký tự ' ch ' không phải là một toán tử. '''

#cơ bản
a = int (input ("Nhập số a: "))
b = int (input ("Nhập số b: "))
ch = input ("Nhập ký tự ch: (+, -, */):  ")
if ch == "+":
    print (f"Kết quả phép tính {a} + {b} = {a + b}")
elif ch == "-":
    print (f"Kết quả phép tính {a} - {b} = {a - b}")
elif ch == "*":
    print (f"Kết quả phép tính {a} * {b} = {a * b}")
elif ch == "/":
    if b != 0:
        print (f"Kết quả phép tính {a} / {b} = {a / b}")
    else:
        print ("Lỗi! Không thể chia cho 0.")
else:
    print (f"Ký tự '{ch}' không phải là một toán tử.")

#nâng cao
try:
    a = float (input ("Nhập số a: "))
    b = float (input ("Nhập số b: "))
    ch = input ("Nhập ký tự ch: (+, -, */):  ")
    
    match ch:
        case "+":
            print (f"Kết quả phép tính {a} + {b} = {a + b}")
        case "-":
            print (f"Kết quả phép tính {a} - {b} = {a - b}")
        case "*":
            print (f"Kết quả phép tính {a} * {b} = {a * b}")
        case "/":
            if b != 0:
                print (f"Kết quả phép tính {a} / {b} = {a / b}")
            else:
                print ("Lỗi! Không thể chia cho 0.")
        case _:
            print (f"Ký tự '{ch}' không phải là một toán tử.")
except ValueError:
    print ("Lỗi! Vui lòng nhập số hợp lệ.")
    
#tối uu
def calculate(a, b, ch):
   match = {
        "+": lambda a, b: a + b,
        "-": lambda a, b: a - b,
        "*": lambda a, b: a * b,
        "/": lambda a, b: a / b if b != 0 else "Lỗi! Không thể chia cho 0."
    }
   return match.get(ch, lambda a, b: f"Ký tự '{ch}' không phải là một toán tử.")(a, b)  

try:
    a = float (input ("Nhập số a: "))
    b = float (input ("Nhập số b: "))
    ch = input ("Nhập ký tự ch: (+, -, */):  ")
    result = calculate(a, b, ch)
    print(f"Kết quả: {result}")
except ValueError:
    print ("Lỗi! Vui lòng nhập số hợp lệ.")
                
