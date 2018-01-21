# Exercise 19 Functions and Variables
def cheese_and_crackers(cheese_count, box_of_crackers):
    print("You have %d cheeses!" %cheese_count)
    print("You have %d boxes of crackers!" %box_of_crackers)
    print("Man that's enough for a party!")
    print("Get a blanket.\n")

print("We can just give the function numbers directly:")
cheese_and_crackers(20,30)


print("OR, we can use variables from our script:")
amount_of_cheese = 10
amount_of_cracker = 50

cheese_and_crackers(amount_of_cheese, amount_of_cracker)


print("We can even do math inside too:")
cheese_and_crackers(10 + 20, 5 + 6)


print("And we can combine the two, variables and math:")
cheese_and_crackers(amount_of_cheese + 100, amount_of_cracker + 1000)

print("we can get directly from user")
a = int(input("a"))
b = int(input("b"))
cheese_and_crackers(a,b)
