'''
 Viết chương trình in ra một chuỗi ký tự bất kỳ. Nội dung chuỗi 
được nhập từ tham số dòng lệnh của chương trình. 
'''
import sys
if len(sys.argv) > 1:
    print("Nội dung chuỗi ký tự là: ", sys.argv[1])
else:
    print("Vui lòng nhập chuỗi ký tự qua tham số dòng lệnh.")
    
