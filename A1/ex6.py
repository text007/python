# 字符串和文本

# 格式化字符串
types_of_people = 10
x = f"There are {types_of_people} types of people."


binary = "binary"
do_not = "don't"
y = f"Those who know {binary} and those who {do_not}."

# 打印输出
print(x)
print(y)

# 打印格式化输出
print(f"I said:{x}")
print(f"I also said:'{y}'")

# 格式化输出拼接
hilarious = False
joke_evaluation = "Isn't that joke so funny?! {}"

# format(): 格式化函数
print(joke_evaluation.format(hilarious))

w = "This is the left side of..."
e = "a string with a right side."

# 字符串拼接
print(w + e)
