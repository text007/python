# 入侵飞船逃生小游戏

from sys import exit        # 错误弹出运行
from random import randint      # 随机打印指定范围内
from textwrap import dedent     # 从字符串的行首删除空白字符

# 场景.类
class Scene(object):

    # 场景的开场.函数
    def enter(self):
        print("This scene is not yet configured.")
        print("Subclass it and implement enter().")
        exit(1) # 有错误退出运行


# 引擎.类
class Engine(object):

    def __init__(self, scene_map):
        self.scene_map = scene_map

    # 运行引擎
    def play(self):
        current_scene = self.scene_map.opening_scene()  # 下一个场景
        last_scene = self.scene_map.next_scene("finished")  # 进入下一个场景

        # 场景描述循环
        while current_scene != last_scene:
            next_scene_name = current_scene.enter()     # 开场描述
            current_scene = self.scene_map.next_scene(next_scene_name)      # 进入下个场景的描述

        # 一定要打印出最后一个场景
        current_scene.enter()


# 死亡.类，继承场景类
class Death(Scene):

    # 死亡描述
    quips = [
        "You died. You kinda suck at this.",
        "Your Mom would be proud...if she were smarter.",
        "Such a luser.",
        "I have a small puppy that's better at this.",
        "You're worse than your Dad's jokes."
    ]

    # 场景的开场.函数
    def enter(self):
        # 随机打印 quips 里的第0到所有个数-1的字符串
        print(Death.quips[randint(0, len(self.quips)-1)])
        exit(1) # 有错误退出运行


# 中央走廊.类，继承场景类
class CentralCorridor(Scene):

    # 开场描述
    def enter(self):
        print(dedent("""
            The Gothons of Planet Percal #25 have invaded your ship and 
            destroyed your entire crew. You are the last surviving 
            member and your last mission is to get the neutron destruct 
            bomb from the Weapons Armory, put it in the bridge, and 
            blow the ship up after getting into an escape pod. 
            
            You're running down the central corridor to the Weapons 
            Armory when a Gothon jumps out, red scaly skin, dark grimy 
            teeth, and evil clown costume flowing around his hate 
            filled body. He's blocking the door to the Armory and 
            about to pull a weapon to blast you.
            """))

        # 玩家回答
        action = input("> ")

        # 玩家答案1
        if action == "shoot!":
            print(dedent("""
                Quick on the draw you yank out your blaster and fire 
                it at the Gothon. His clown costume is flowing and 
                moving around his body, which throws off your aim. 
                Your laser hits his costume but misses him entirely. 
                This completely ruins his brand new costume his mother 
                bought him, which makes him fly into an insane rage 
                and blast you repeatedly in the face until you are 
                dead. Then he eats you.
                """))
            # 返回 死亡
            return 'death'

        # 玩家答案2
        elif action == "dodge!":
            print(dedent("""
                Like a world class boxer you dodge, weave, slip and 
                slide right as the Gothon's blaster cranks a laser 
                past your head. In the middle of your artful dodge 
                your foot slips and you bang your head on the metal 
                wall and pass out. You wake up shortly after only to 
                die as the Gothon stomps on your head and eats you.
                """))
            # 返回 死亡
            return "death"

        # 玩家答案3
        elif action == "tell a joke":
            print(dedent("""
                    Lucky for you they made you learn Gothon insults in 
                    the academy. You tell the one Gothon joke you know: 
                    Lbhe zbgure vf fb sng, jura fur fvgf nebhaq gur ubhfr, 
                    fur fvgf nebhaq gur ubhfr. The Gothon stops, tries 
                    not to laugh, then busts out laughing and can't move. 
                    While he's laughing you run up and shoot him square in
                    the head putting him down, then jump through the 
                    Weapon Armory door.
                    """))
            # 返回 激光武器盔甲
            return "laser_weapon_armory"

        # 玩家答案4
        else:
            print("does not compute!")
            # 返回 中心部位
            return "central_corridor"


# 激光武器军械库.类，继承场景类
class LaserWeaponArmory(Scene):

    # 开场描述
    def enter(self):
        print(dedent("""
            You do a dive roll into the Weapon Armory, crouch and scan 
            the room for more Gothons that might be hiding. It's dead 
            quiet, too quiet. You stand up and run to the far side of 
            the room and find the neutron bomb in its container. 
            There's a keypad lock on the box and you need the code to 
            get the bomb out. If you get the code wrong 10 times then 
            the lock closes forever and you can't get the bomb. The 
            code is 3 digits.
            """))

        # 随机生成 1-9 的 3 个数字组合
        code = f"{randint(1,9)}{randint(1,9)}{randint(1,9)}"
        print("开门密码", code)
        # 玩家输入
        guess = input("[keypad]> ")
        guesses = 1

        # 玩家输入密码循环
        while guess != code and guesses < 10:
            print("密码错误，清重新输入!")
            guesses += 1
            guess = input("[keypad]> ")

        if guess == code:
            print(dedent("""
                The container clicks open and the seal breaks, letting 
                gas out. You grab the neutron bomb and run as fast as 
                you can to the bridge where you must place it in the 
                right spot.
                """))
            # 返回 正桥
            return "the_bridge"

        else:
            print(dedent("""
                The lock buzzes one last time and then you hear a 
                sickening melting sound as the mechanism is fused 
                together. You decide to sit there, and finally the 
                Gothons blow up the ship from their ship and you die.
                """))
            # 返回 死亡
            return "death"


# 桥.类，继承场景类
class TheBridge(Scene):

    # 开场描述
    def enter(self):
        print(dedent("""
            You burst onto the Bridge with the netron destruct bomb 
            under your arm and surprise 5 Gothons who are trying to 
            take control of the ship. Each of them has an even uglier 
            clown costume than the last. They haven't pulled their 
            weapons out yet, as they see the active bomb under your
            arm and don't want to set it off.
            """))
        # 玩家输入
        action = input("> ")

        if action == "throw the bomb":
            print(dedent("""
                In a panic you throw the bomb at the group of Gothons 
                and make a leap for the door. Right as you drop it a 
                Gothon shoots you right in the back killing you. As 
                you die you see another Gothon frantically try to 
                disarm the bomb. You die knowing they will probably 
                blow up when it goes off.
                """))
            # 返回 死亡
            return "death"

        elif action == "slowly place the bomb":
            print(dedent("""
                You point your blaster at the bomb under your arm and 
                the Gothons put their hands up and start to sweat. 
                You inch backward to the door, open it, and then 
                carefully place the bomb on the floor, pointing your 
                blaster at it. You then jump back through the door, 
                punch the close button and blast the lock so the 
                Gothons can't get out. Now that the bomb is placed 
                you run to the escape pod to get off this tin can.
                """))
            # 返回 逃生舱
            return "escape_pod"

        else:
            print("DOES MOT COMPUTE!")
            return "the_bridge"


# 逃生舱.类，继承场景类
class EscapePod(Scene):

    # 开场描述
    def enter(self):
        print(dedent("""
            You rush through the ship desperately trying to make it 
            the escape pod before the whole ship explodes. It seems 
            like hardly any Gothons are on the ship, so your run is 
            clear of interference. You get to the chamber with the 
            escape pods, and now need to pick one to take. Some of 
            them could be damaged but you don't have time to look. 
            There's 5 pods, which one do you take? 
            """))

        # 随机 1-5 的数字
        good_pod = randint(1, 5)
        print("随机数字", good_pod)
        guess = input("[pod #]> ")

        if int(guess) != good_pod:
            print(dedent("""
                You jump into pod {guess} and hit the eject button. 
                The pod escapes out into the void of space, then 
                implodes as the hull ruptures, crushing your body into 
                jam jelly.
                """))
            # 返回死亡
            return "death"

        else:
            print(dedent("""
                You jump into pod {guess} and hit the eject button. 
                The pod easily slides out into space heading to the 
                planet below. As it flies to the planet, you look 
                back and see your ship implode then explode like a 
                bright star, taking out the Gothon ship at the same 
                time. You won!
                """))
            #
            return "finished"


# 结束.类，继承场景类
class Finished(Scene):

    # 开场描述
    def enter(self):
        print("You won! Good job.")
        return "finished"


class Map(object):

    scenes = {
    'central_corridor': CentralCorridor(),  # 中央走廊
    'laser_weapon_armory': LaserWeaponArmory(), # 激光武器军械库
    'the_bridge': TheBridge(),  # 桥
    'escape_pod': EscapePod(),  # 逃生舱
    'death': Death(),   # 死亡
    'finished': Finished(), # 游戏结束
    }

    def __init__(self, start_scene):
        self.start_scene = start_scene

    # 进入下一个场景函数
    def next_scene(self, scene_name):
        val = Map.scenes.get(scene_name)
        return val

    # 下一个场景开始函数
    def opening_scene(self):
        return self.next_scene(self.start_scene)


# 测试代码
a_map = Map("laser_weapon_armory")
a_game = Engine(a_map)
a_game.play()
