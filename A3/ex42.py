

## Animal is-a object (yes, sort of confusing) look at the extra ceadit
class Animal(object):
    pass

## dog is-a animal
class Dog(Animal):

    def __init__(self, name):
        ## dog has-a name
        self.name = name

## cat is-a animal
class Cat(Animal):

    def __init__(self, name):
        ## cat has-a name
        self.name = name

## person is-a object
class Person(object):

    def __init__(self, name):
        ## Person has-a name
        self.name = name

        ## person has-a pet of some kind
        self.pet = None

## employee is-a person
class Employee(Person):

    def __init__(self, name, salary):
        ## employee has-a name/employee has-a salary hmm what is this strange magic?
        super(Employee, self).__init__(name)
        ## employee has-a salary
        self.salary = salary

## fish is-a object
class Fish(object):
    pass

## salmon is-a fish
class Salmon(Fish):
    pass

## halibut is-a fish
class Halibut(Fish):
    pass

## rover is-a dog
rover = Dog("Rocer")

## satan is-a cat
satan = Cat("Satan")

## mary is-a person
mary = Person("mary")

## mary pet is-a satan
mary.pet = satan

## ??
frank = Employee("Frank", 120000)

## ??
frank.pet = rover

##??
filpper = Fish()

##??
crouse = Salmon()

## ??
harry = Halibut()
