# 复制一个文件内容到另外一个文件中

# 导入 sys 的 argv 模块
from sys import argv
# 导入 os.path 的 exists 模块
# 基于一个字符串里面的变量文件名来判断，如果一个文件存在，它就会返回 True ，不存在就会返回 False
from os.path import exists

# 获取文件名
script, from_file, to_file = argv

# 打印引入文件名字符串
print(f"Copying from {from_file} to {to_file}")

# 打开文件
# we could do these two on one line,how?
in_file = open(from_file)
# 读取文件内容并赋值
indata = in_file.read()

# 打印显示文件中字符串的长度
# len():取字符串的长度
print(f"the input file is {len(indata)} bytes long")

# 判断文件是否存在
print(f"Does the output file exist? {exists(to_file)}")
print("Ready, hit RETURN to continue.CTRL-C to abort.")
# 用户输入
input()

# 打开文件用于写入
out_file = open(to_file, "w")
# 写入文件内容
out_file.write(indata)

# 打印字符串
print("Alright, all dore.")

# 关闭文件
out_file.close()
in_file.close()
