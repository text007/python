# 阅读文件
# open()：用于打开一个文件，创建一个 file 对象
# read()：用于从文件读取指定的字节数，如果未给定或为负则读取所有。

# 导入 sys 的 argv 模块
from sys import argv

# 获取文件名
script, filename = argv

# 打开一个文件
txt = open(filename)

# 打印
print(f"Here's your file {filename}:")
# 读取文件字节数
print(txt.read())

# 打印
# print("Type the filename again:")
# # 用户输入
# file_again = input("> ")
#
# # 打开一个文件
# txt_again = open(file_again)
#
# # 读取文件字节数
# print(txt_again.read())
