alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
direction = input("Type 'encode' to encrypt, type 'decode' to decrypt: \n")
text = input("Type your message : \n")
shift = int(input("Type the shift number : \n"))

# creating a function to encrypt
def encrypt(plain_text, shift_amount):
    cipher_text = ""
    for letter in plain_text:
        position = alphabet.index(letter)
        new_position = position + shift
        new_letter = alphabet[new_position]
        cipher_text = cipher_text + new_letter
    print(f"The encoded text is {cipher_text} ")

# creating decrypt function
def decrypt(cipher_text, shift_amount):
    plain_text = ""
    for letter in cipher_text:
        position = alphabet.index(letter)
        new_position = position - shift_amount
        plain_text = plain_text + alphabet[new_position]
    print(f"The decoded text is {plain_text}")

# to check whether to encrypt or decrypt
if direction == "encode":
        # calling the encrypt function
        encrypt(plain_text=text, shift_amount=shift)
elif direction == "decode":
        # calling the decrypt function
        decrypt(cipher_text=text, shift_amount=shift)
else:
        print("Enter a valid Answer")



