# argv 和 input() 结合

from sys import argv
third, script, first, second = argv

print("你的出生年份？", script)
print("你的出生月份？", first)
print("你的出生日期？", second)

family_name = input("你的姓氏？")
name = input("你的名字？")

print(f"你的姓名：{family_name} {name}")
