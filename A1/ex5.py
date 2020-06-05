# 格式字符串： 字符串中 {}
# f" ": 告诉 python 该字符串需要被格式化

name = "Zed A. Shaw"
age = 35 # not a lie
height = 74 # inches
weight = 180 # lbs
eyes = "blue"
teeth = "white"
hair = "Brown"

print(f"Let's talk about {name}.")
print(f"He's {height} inches tall.")
print(f"He's {weight} pounds heavy.")
print("Actually that's not too heavy.")
print(f"He's got {eyes} eyes and {hair} hair")
print(f"He's teeth are usually {teeth} depending on the coffee.")

# this line is tricky, try to get to get it exactly righr
total = age + height + weight
print(f"If I dd {age}, {height}, and {weight} I get {total}.")
