# 操作列表

ten_thins = "Apples Oranges Crows Telephone Light Sugar"

print("Wait there are not 10 things in that list. let's fix it.")

# split(" "):指定分隔符对字符串进行切片，如果参数 num 有指定值，则分隔 num+1 个子字符串
stuff = ten_thins.split(" ")
more_stuff = ["Day", "Night", "Song", "Frisbee", "Corn", "Banana", "Girl", "Boy"]

# 循环遍历
while len(stuff) != 10:
    # pop(): 移除列表中的一个元素（默认最后一个元素），并且返回该元素的值。
    next_one = more_stuff.pop()
    print("Adding: ", next_one)
    # append( ):在列表末尾添加新的对象
    stuff.append(next_one)
    # len( ):返回对象（字符、列表、元组等）长度或项目个数。
    print(f"There are {len(stuff)} items now.")

print("There we go: ", stuff)

print("Let's do some things with stuff.")

print(stuff[1])
print(stuff[-1])
# pop(): 移除列表中的一个元素（默认最后一个元素），并且返回该元素的值。
print(stuff.pop())
# join( ):将序列中的元素以指定的字符连接生成一个新的字符串
print(" ".join(stuff))
print("#".join(stuff[3:5]))
