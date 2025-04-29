

# 10

# yil = int(input("Yilni kiriting: "))

# if (yil % 4 == 0 and yil % 100 != 0) or (yil % 400 == 0):
#     print("Natija: true")
# else:
#     print("Natija: false")


# 11

# c = input("Belgini kiriting: ")

# if '0' <= c <= '9':
#     print("Natija: son")
# else:
#     print("Natija: alpha")


# 12

# c = input("Belgini kiriting: ")

# if 'a' <= c <= 'z':
#     print("Natija: lowerCase")
# elif 'A' <= c <= 'Z':
#     print("Natija: upperCase")
# else:
#     print("Natija: none")


# 13

# son=input("son kirit: ")

# if son == '1':
#     print("Dushanba")
# elif son =='2':
#     print("Seshanba")
# elif son == '3':
#     print("Chorshanba")
# elif son == '4':
#     print("Payshanba")
# elif son == '5':
#     print("Juma")
# elif son == '6':
#     print("Shanba")
# elif son == '7':
#     print("Yakshanab")
# else:
#     print("none")


# 14

# qoida:

# Uchburchakning ichki burchaklari yig‘indisi 180° bo‘lishi kerak.

# Demak, berilgan a, b, c sonlari yig‘indisi 180° ga teng bo‘lsa — bu uchburchakning burchaklari bo‘la oladi.


# a = int(input("a burchakni kiriting: "))
# b = int(input("b burchakni kiriting: "))
# c = int(input("c burchakni kiriting: "))

# if a + b + c == 180 and a > 0 and b > 0 and c > 0:
#     print("true.")
# else:
#     print("false")



# 15

# a + b > c

# a + c > b

# b + c > a


# a = int(input("a tomonni kiriting: "))
# b = int(input("b tomonni kiriting: "))
# c = int(input("c tomonni kiriting: "))

# if a + b > c and a + c > b and b + c > a:
#     print("true")
# else:
#     print("false")



# 17


# a = int(input("a sonini kiriting: "))
# b = int(input("b sonini kiriting: "))
# c = int(input("c sonini kiriting: "))

# count = 0


# if a > 0:
#     print(a)
#     count += 1
# if b > 0:
#     print(b)
#     count += 1
# if c > 0:
#     print(c)
#     count += 1

# print("Musbat sonlar soni:", count)



# 18


# a = int(input("a sonini kiriting: "))
# b = int(input("b sonini kiriting: "))

# if a == b:
#     print("Ikkalasi teng")
# else:
#     print("Kichik son:", min(a, b))



# 2-usuli:


# a = int(input("a sonini kiriting: "))
# b = int(input("b sonini kiriting: "))

# if a < b:
#     print("Kichik son:", a)
# elif b < a:
#     print("Kichik son:", b)
# else:
#     print("Ikkalasi teng")



# 19



# a = int(input("a sonini kiriting: "))
# b = int(input("b sonini kiriting: "))
# c = int(input("c sonini kiriting: "))

# qiymat = (a + b + c) // 3

# print("O'rtacha qiymat:", qiymat)
