# 读写文件

# close - 关闭文件，就像编辑器中的 “文件->另存为”一样。
# read - 读取文件内容。你可以把读取结果赋给一个变量。
# readline - 只读取文本文件的一行内容。
# truncate - 清空文件。清空的时候要当心。
# write('stuff') - 给文件写入一些“东西”。
# seek(0) - 把读/写的位置移到文件最开头。

# r	    以只读方式打开文件。文件的指针将会放在文件的开头。这是默认模式。
# rb	以二进制格式打开一个文件用于只读。文件指针将会放在文件的开头。这是默认模式。
# r+	打开一个文件用于读写。文件指针将会放在文件的开头。
# rb+	以二进制格式打开一个文件用于读写。文件指针将会放在文件的开头。
# w	    打开一个文件只用于写入。如果该文件已存在则打开文件，并从开头开始编辑，即原有内容会被删除。如果该文件不存在，创建新文件。
# wb	以二进制格式打开一个文件只用于写入。如果该文件已存在则打开文件，并从开头开始编辑，即原有内容会被删除。如果该文件不存在，创建新文件。
# w+	打开一个文件用于读写。如果该文件已存在则打开文件，并从开头开始编辑，即原有内容会被删除。如果该文件不存在，创建新文件。
# wb+	以二进制格式打开一个文件用于读写。如果该文件已存在则打开文件，并从开头开始编辑，即原有内容会被删除。如果该文件不存在，创建新文件。
# a	    打开一个文件用于追加。如果该文件已存在，文件指针将会放在文件的结尾。也就是说，新的内容将会被写入到已有内容之后。如果该文件不存在，创建新文件进行写入。
# ab	以二进制格式打开一个文件用于追加。如果该文件已存在，文件指针将会放在文件的结尾。也就是说，新的内容将会被写入到已有内容之后。如果该文件不存在，创建新文件进行写入。
# a+	打开一个文件用于读写。如果该文件已存在，文件指针将会放在文件的结尾。文件打开时会是追加模式。如果该文件不存在，创建新文件用于读写。
# ab+	以二进制格式打开一个文件用于追加。如果该文件已存在，文件指针将会放在文件的结尾。如果该文件不存在，创建新文件用于读写。



# 导入 sys 的 argv 模块
from sys import argv

# argv 获取文件名
script, filename = argv

# 打印字符串引入文件名
print(f"We're going to erase {filename}")
print("If you don't want that, hit CTRL-C (^C).")
print("If you do want that, hit RETURN.")

# 用户输入
input("?\n")

# 打印字符串
print("Opening the file...")
# （open（））打开文件（"w"）用于打开/新建文件只写入
target = open(filename, "w")

# 打印字符串
print("Truncating the file. Goodbye!")
# 清空文件内容
target.truncate()

# 打印字符串
print("Now I'm going to ask you for three lines.")

# 用户输入
line1 = input("line 1:")
line2 = input("line 2:")
line3 = input("line 3:")

# 打印字符串
print("I'm going to write these to the file.")

# 写入用户输入的内容
target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

# 打印字符串
print("And finally, we close it.")
# 关闭文件
target.close()