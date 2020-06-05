# 简化 ex17

from sys import argv
# from os.path import exists

script, file1, file2 = argv

in_file1 = open(file1, encoding="utf-8")
indata = in_file1.read()

in_file2 = open(file2, "w")
in_file2.write(indata)

in_file1.close()
in_file2.close()
