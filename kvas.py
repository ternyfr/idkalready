# for i in range (1, 101):
#     print(i)

# i = 0
# while False:
#     i = i + 1
#     if i % 101 == 0:
#         print(i)

# ch = int(input("введи первое число:"))
# chh = int(input("введи второе число, оно должно быть больше первого:"))
# if ch > chh:
#     print("неверные данные")
# else:
#     print("диапозон чисел:")
#     for i in range(ch, chh+1):
#         print(i)

# s = 0
# print("вводи числа:")
# while True:
#     n = int(input())
#     if n % 4 == 0 or n % 3 == 0 or n % 6 == 0:
#         s = s + n
#     if n == 0:
#         print("сумма всех чисел:", s)
#         break

pi = 3
a = 2
for i in range(1, 16):
    if i % 2 == 0:
        pi = pi - 4 / (a * (a+1) * (a+2))
    else:
        pi = pi + 4 / (a * (a+1) * (a+2))
    a += 2
print(pi)