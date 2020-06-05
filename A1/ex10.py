# 转义字符
# \n：换行符
# \t：tab（四个空格）
# \：转义字符（把没法输入的字符转化成字符串）

tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line."
backslash_cat = "I'm \\ a \\ cat."

fat_cat = """
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass \\I's
"""

print(tabby_cat)
print(persian_cat)
print(backslash_cat)
print(fat_cat)
