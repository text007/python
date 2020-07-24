# 显式继承


class Parent(object):

    def override(self):
        print("PARENT override()")


class Child(Parent):

    def override(self):
        print("CHILE override()")


dad = Parent()
son = Child()

dad.override()
son.override()
