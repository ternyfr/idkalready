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

# pi = 3

a = ""
wishlist = []
while a != "0":
    a = input("\nчто хочешь записать? 0 - выйход из программы\n")
    if a != "0":
        wishlist.append(a)
print("добавлено в корзину:")

def spisok():
    i = 0
    n = 1
    while i < len(wishlist):
        print(f"{n}. {wishlist[i]}")
        i += 1
        n += 1

spisok()
b = ""
while b != 0:
    b = input("\nесли хочешь удалить элемент из списка, введи его номер. 0 - конец программы\n")
    if b != 0:
        wishlist.pop(b-1)
    spisok()
# a = 2
# for i in range(1, 16):
#     if i % 2 == 0:
#         pi = pi - 4 / (a * (a+1) * (a+2))
#     else:
#         pi = pi + 4 / (a * (a+1) * (a+2))
#     a += 2
# print(pi)

# string = "привет. мир, это я, почтальон печкин"

def stringReplace(string):
    string2 = ""
    for i in range(0, len(string)):
        if string[i] == "a":
            string2 += "G"
        elif string[i-1] == " " or i == 0:
            string2 += string[i].capitalize()
        else:
            string2 += string[i]
    print(string2)

stringReplace("lhdfkiafoi diuapsd udoaud aosddupj qu ad u")
