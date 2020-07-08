# 名称，变量，代码，函数
# def 创建函数

# *args：告诉 Python 取所有的参数给函数
def print_two(*args):
    arg1, arg2 = args
    print(f"arg1: {arg1}, arh2: {arg2}")

def print_two_again(arg1, arg2):
    print(f"arg1: {arg1}, arh2: {arg2}")

def print_one(arg1):
    print(f"arg1: {arg1}")

def print_none():
    print("I got nothin'.")

print_two("Zed", "Shaw")
print_two_again("Zed", "Shaw")
print_one("First!")
print_none()
