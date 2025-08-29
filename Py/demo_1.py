print ('hello world from demo_1.py')

#  số hoàn hảo
for c in 'Python': 
    print(c, end='-') 
    
n = int(input('Nhập số n: ')) 
s = 0 
for i in range(1,n): 
    if n % i == 0:  
        s = s + i 
if s == n: 
    print(n, ' là số hoàn hảo') 
else: 
    print(n, ' không là số hoàn hảo') 