#  10 种不同的方式运行函数

def exercise(*args):
    print(args)

exercise(1, 3)

L1, L2 = 3, 99
exercise(L1, L2)

exercise(L1 + L2)

exercise(L1 + 2, L2 - 9)

L3 = 55 + 66
exercise(L3)

L4 = 2 >= 3
exercise(L4)

exercise(input("年龄?"))

file = open("test.txt")
cuntent2 = file.read()
exercise(cuntent2)
file.close()
