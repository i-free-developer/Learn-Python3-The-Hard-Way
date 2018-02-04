# Exercise 44 Inheritance vs. Composition
# Implicit Inheritance
class Parent(object):

  def implicit(self):
      print("Parent implicit()")

class Child(Parent):
    pass

dad = Parent()
son = Child()

dad.implicit()
son.implicit()



