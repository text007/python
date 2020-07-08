# return：函数返回值

# 创建函数传入两个参数，打印两参数，返回两个参数之和
def add(a, b):
    print(f"ADDING {a} + {b}")
    return a + b

# 创建函数传入两个参数，打印两参数，返回两个参数之差
def subtrct(a, b):
    print(f"SUBTRACTING {a} - {b}")
    return a - b

# 创建函数传入两个参数，打印两参数，返回两个参数之积
def multiply(a, b):
    print(f"MULTIPLYING {a} * {b}")
    return a * b

# 创建函数传入两个参数，打印两参数，返回两个参数之余数
def divide(a, b):
    print(f"DIVIDING {a} / {b}")
    return a / b

print("------")

# 给函数传入两个值，并对返回结果进行赋值
age = add(30, 5)
height = subtrct(78, 4)
weight = multiply(90, 2)
iq = divide(100, 2)

# 打印返回值的字符串
print(f"Age:{age}, Height:{height}, Weight:{weight}, IQ:{iq}")

print("========")

# 给函数传入函数，并对返回结果进行赋值
what = add(age, subtrct(height, multiply(weight, divide(iq, 2))))

# 打印返回值
print(what)
