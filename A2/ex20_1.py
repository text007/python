# 函数与文件

# 导入 sys 的 argv 模块
from sys import argv

# 获取文件名
script, input_file = argv

# 创建函数传入读取的文件内容作为参数，并打印出来
def print_all(f):
    print(f.read())

# 创建函数，传入文件作为参数，把读/写的位置移到文件最开头
# seek(0) ：把读/写的位置移到文件最开头。
def rewind(f):
    f.seek(0)

# 创建函数，传入两个参数
def print_a_line(line_count, f):
    # 打印一个参数和文件内容的一行
    print(line_count, f.readline())

# 打开文件
current_file = open(input_file)

# 打印字符串并换行
print("First let's print the whole file:\n")

# 传入参数
print_all(current_file)

# 打印字符串
print("Now let's rewind, kind of like a tape.")

# 传入参数
rewind(current_file)

# 打印字符串
print("Let's print three lines:")

# 赋值，传入参数
current_line = 1
print_a_line(current_line, current_file)

# 赋值，传入参数
current_line += 1 # current_line = 2
print_a_line(current_line, current_file)

# 赋值，传入参数
current_line += 1 # current_line = 3
print_a_line(current_line, current_file)
