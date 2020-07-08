# 练习

def fire():
        print("这里是火门，请回答问题继续游戏。")
        print("你喜欢火吗？")

        key = input("> ")

        if key == "喜欢":
            print("你被火烧死")

        elif key == "不喜欢":
            print("将进入冰的世界")
            ice()

        else:
            print("回答有误！ 将退出游戏。")

def ice():
        print("这里是冰门，请回答问题继续游戏。")
        print("你喜欢冰吗？")

        key = input("> ")

        if key == "喜欢":
            print("你被冰块冻住")

        elif key == "不喜欢":
            print("将进入风的世界")
            wind()

        else:
            print("回答有误！ 将退出游戏。")

def wind():
    print("这里是风门，请回答问题继续游戏。")
    print("你喜欢风吗？")

    key = input("> ")

    if key == "喜欢":
        print("你被风吹飞")

    elif key == "不喜欢":
        print("将进入土的世界")
        soil()

    else:
        print("回答有误！ 将退出游戏。")

def soil():
    print("这里是土门，请回答问题继续游戏。")
    print("你喜欢土吗？")

    key = input("> ")

    if key == "喜欢":
        print("你被埋在土里")

    elif key == "不喜欢":
        print("")

    else:
        print("回答有误！ 将退出游戏。")

print("游戏开始！")
print("即将进入房间，请选择你想进入的房间号？")
print("1号门：火门， 2号门：冰门，3号门：风门，4号门：土门，")

while True:

    number = input("> ")
    if number == "1" and "1号门":
        fire()
        break

    elif number == "2" and "2号门":
        ice()
        break

    elif number == "3" and "3号门":
        wind()
        break

    elif number == "4" and "4号门":
        soil()
        break

    else:
        print("请选择正确门号")
        print("1号门：火门， 2号门：冰门，3号门：风门，4号门：土门，")
