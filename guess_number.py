#hard-level (mixing up the order of letters, symbols and numbers)


password_list = []

for char in range(1, number_letters + 1):
    password_list.append(random.choice(letters))

for char in range(1, number_symbols + 1):
    password_list.append(random.choice(symbols))

for char in range(1, number_numbers + 1):
    password_list.append(random.choice(numbers))

random.shuffle(password_list)
print(password_list)

#to convert list into string

password = ""
for char in password_list:
     password += char

print(f"your password is : {password}")
