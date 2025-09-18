#) Dãy tất cả các số là bội của 3 và nhỏ hơn 100:
lst_1  = [x for x in range (100) if x % 3 == 0]

# b) Dãy 20 số chính phương đầu tiên:
list_2 = [i * i  for i in range (1, 21)]

# Dãy 10 chuỗi nhị phân theo quy luật 1, 10, 100...:
list_3 = [str(10**i) for i in range (10)

# d) Dãy 10 chuỗi nhị phân theo quy luật 100000000, 010000000,...:
list_4 = [format(1<< (9 -i), '09b')for i in range (10)]