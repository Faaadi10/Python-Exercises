import random

letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
symbols = ['!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`', '{', '|', '}', '~']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

print("Password Generator")
number_letters = int(input("Enter how many letters do you require"))
number_numbers = int(input("Enter how many numbers do you require"))
number_symbols = int(input("Enter how many numbers do you require"))

#easy-level

password = ""
for char in range(1, number_letters + 1):
    password = password + random.choice(letters)

for char in range(1, number_letters + 1):
    password = password + random.choice(numbers)

for char in range(1, number_letters + 1):
    password = password + random.choice(symbols)

print("Your Password is : " + password)
