# 总结练习

# 打印字符串加特殊字符
print("Let's practice everything.")
print("You\'d need to know \'bout escapes with \\ that do:")
print("\n newlines and \t tabs")

poem = """
\t The lovely world
with logic so firmly planted
cannot discern \n the needs of love
nor comprehend passion from intuition
and requires an explanation
\n\t\twhere there is none."""

print("————————")
print(poem)
print("————————")

# 格式化字符串
five = 10 - 2 + 3 - 6
print(f"This should be five: {five}")

# 定义一个函数传入一个参数，得出返回值
def secret_formula(started):
    jelly_beans = started * 500
    jars = jelly_beans / 1000
    crates = jars / 100
    return jelly_beans, jars, crates

# 赋值，给函数传入参数得出返回值
start_point = 10000
beans, jars, crates = secret_formula(start_point)

# 格式化传入参数的字符串传入参数 .format() 方法
# remember that this is another way to format a string
print("with a starting point of:{}".format(start_point))
# 格式化传入参数的字符串传入参数 .f"{}" 方法
# it's just like with an f"" string
print(f"we'd have {beans} beans, {jars} jars, and {crates} crates.")

# 赋值运算
start_point = start_point / 10

# 格式化传入参数的字符串传入参数 .format() 方法（*：传入所有需要的参数）。
print("we can also do that this way:")
formula = secret_formula(start_point)
# this is an easy wat to apply a list to a format string
print("we'd have {} beans, {} jars, and {} crates.".format(*formula))
