import random

print("Tab Splitter")
names_string = input("Give me the names of everyone, separated by a comma\n")
names = names_string.split(",")
number = len(names)
random = random.randint(0, number - 1)
print(random)
print(names[random] + " will have to pay the bill")
