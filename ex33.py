# Exercise 33 While - Loops
i = 0
numbers = []
while i < 6:
    print("At the top i is %d" %i)
    numbers.append(i)

    i += 1
    print("Numbers now:", numbers)
    print("At the bottom i is %d" %i)


print("The numbers:")

for x in numbers:
  print(x)

def make_list(n, step):
    i = 0
    numbers = []
    while i < n:
        numbers.append(i)
        i += step
    print("The list is:", numbers)

make_list(100,7)
