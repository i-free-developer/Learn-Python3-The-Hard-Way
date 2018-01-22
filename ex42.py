# Exercise Is-A, Has-A, Objects and Classes
# Animal is-a object
class Animal(object):
    pass
# Dog is-a object
class Dog(Animal):

    def __init__(self, name):
        ##??
        self.name = name

# Cat is-a object
class Cat(Animal):

    def __init__(self, name):
        ## ??
        self.name = name

# Person is-a object
class Person(object):

    def __init__(self, name):
        ##??
        self.name = name

        ## person has-a pet of some kind
        self.pet = None

# Employee is-a object
class Employee(Person):

    def __init__(self, name, salary):
        ## ?? what is this strange magic?
        super(Employee, self).__init__(name)
        ##??
        self.salary = salary

# Fish is-a object
class Fish(object):
    pass

# Salmon is-a fish
class Salmon(Fish):
    pass

# Halibut is-a fish
class Halibut(Fish):
    pass


## rover is-a dog
rover = Dog("Rover")

## satan is-a cat
satan = Cat("Satan")

# mary is-a person
mary = Person('Mary')

## mary has-a pet which is satan
mary.pet = satan

## frank is-a employee
frank = Employee('Frank', 120000)

## frank has-a pet which is rover
frank.pet = rover

## fliper is-a fish
fliper = Fish()

## crouse is-a Salmon
crouse = Salmon()

## harry is-a Halibut
harry = Halibut()
























