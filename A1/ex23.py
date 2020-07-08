# 字符串编码与解码

import sys
script, encoding, error = sys.argv

# 定义函数传入三个参数
def main(language_file, encoding, errors):
    # 从给出的 languages 文件中读取一行
    line = language_file.readline()

    # 当读取文件有内容，则继续；反之则跳出
    if line:
        # 调用 print_line 函数
        print_line(line, encoding, errors)
    # 调用 main 函数做循环作用
    return main(language_file, encoding, errors)

# 定义 print_line 函数：用来编码 languages.txt 文件中的每一行内容
def print_line(line, encoding, errors):
    # 给读取文件内容移除字符串头尾指定的字符（默认为空格或换行符）或字符序列
    next_lang = line.strip()
    # 对获得的文件字符串进行编码
    # .encode（）：返回编码字符串
    raw_bytes = next_lang.encode(encoding, errors=errors)
    # 对编码字符串进行解码
    # .decode（）：返回解码字符串
    cooked_string = raw_bytes.decode(encoding, errors=errors)

    # 打印编码字符串和解码字符串
    print(raw_bytes, "<===>", cooked_string)

# 打开读取文件
languaes = open("languages.txt", encoding="utf-8")

# 传入参数调用
main(languaes, encoding, error)
