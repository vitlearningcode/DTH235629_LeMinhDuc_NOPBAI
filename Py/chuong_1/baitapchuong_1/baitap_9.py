'''
Hãy in ra màn hình hình chữ nhật như dưới đây: 
* * * * * * * * * 
* * * * * * * * * 
* * * * * * * * * 
* * * * * * * * *
'''
for i in range(4):
    for j in range(9):
        print('*', end=' ')
    print() 
# Hoặc
print(('* ' * 9 + '\n') * 4)
# Hoặc
print(('* ' * 9 + '\n') * 4, end='')
# Hoặc
print(('* ' * 9 + '\n') * 4, sep='')
# Hoặc
print(('* ' * 9 + '\n') * 4, sep='', end='')
