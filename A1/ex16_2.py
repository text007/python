# 简化 ex16 练习

from sys import argv

script, filename = argv

new = open(filename, "w")
new.truncate()

new.write(input("L1内容？"))
new.write("\n")
new.write(input("L2内容？"))
new.write("\n")
new.write(input("L3内容？"))
new.write("\n")

new.close()
