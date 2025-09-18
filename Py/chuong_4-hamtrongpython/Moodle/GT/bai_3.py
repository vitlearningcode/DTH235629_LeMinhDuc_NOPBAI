#Viết hàm tính N!

#1
def factorial_basic (n):
    result = 1
    for i in range (1, n + 1):
        result *= i
    return result
print (factorial_basic(5))

def factorial_recursive (n):
    if n == 0 or n == 1:
        return 1
    return n * factorial_recursive(n - 1)
print (factorial_recursive(5))

