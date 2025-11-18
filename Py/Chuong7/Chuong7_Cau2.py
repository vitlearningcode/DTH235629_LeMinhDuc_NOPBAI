#Xử lí file
def LuuFile(path,data):
    file=open(path,'a',encoding='utf-8')
    file.writelines(data)
    file.writelines("\n")
    file.close()
def DocFile(path):
    arrSo=[]
    file=open(path,'r',encoding='utf-8')
    for line in file:
        data=line.strip()
        arr=data.split(',')
        arrSo.append(arr)
    file.close()    
    return arrSo
    
#Test lưu file
LuuFile("csdl_so.txt","-5,4,7,9,3,20")
LuuFile("csdl_so.txt","5,-4,37,-19,24,-21")
LuuFile("csdl_so.txt","15,9,0,-38,-3,15")
LuuFile("csdl_so.txt","5,-4,77,-9,3,-7")
LuuFile("csdl_so.txt","55,44,27")
LuuFile("csdl_so.txt","-50,26")
#Test đọc file
arrSo=DocFile("csdl_so.txt")
print(arrSo)
def XuatSoAmTrenMoiDong(arrSo):
    for row in arrSo:
        for element in row:
            number=int(element)
            if number<0:
                print(number,end='\t')
        print()
print("Các số âm trên mỗi dòng:")
XuatSoAmTrenMoiDong(arrSo)



