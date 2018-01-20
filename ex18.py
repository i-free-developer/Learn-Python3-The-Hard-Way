# Exercise 18 Names, variables, Code, Functions
# This one is like your scripts with argv
def print_two(*args):
  arg1, arg2 = args
  print("arg1: %r, arg2: %r" %(arg1, arg2))

# ok, that *arg is actually pointless, we can just di this
def print_two_again(arg1, arg2):
  print("arg1: %r, arg2: %r" %(arg1, arg2))

# this just takes one argument
def print_one(arg1):
  print("arg1: %s" %arg1)

# this one takes no arguments
def print_none():
  print("I got nothing.")

print_two("Xiaohu", "Pei")
print_two_again("xiaohu","pei")
print_one("first")
print_none()
