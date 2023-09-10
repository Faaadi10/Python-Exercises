# defining the function

def isprime(number):
    if number<=1:
        return False # Numbers less than or equal to 1 are not prime

    for i in range (2, int(number**5) + 1):
        if number%i == 0:
            return False
        else:
            return True

# Calling the function
user_num = int(input("Enter your Number"))
if isprime(user_num) == True:
    print("Prime number")
else:
    print("Not prime number")

