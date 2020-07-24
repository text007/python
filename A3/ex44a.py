# 隐式继承


class Parent(object):

    def implicit(self):
        print("PARENT implicit()")


class Child(Parent):
        pass
        # def override(self):
        # print("CHILE override()")


dad = Parent()
son = Child()

dad.implicit()
son.implicit()
