import random
import string

print("|=====.... RANDOM PASSWORD GENERATOR ....=====|")

length = int(input("Enter password length: "))
if length < 4:
    print("Password should be at least 4 characters long.")
    exit()
    if length > 20:
        print("Password should not exceed 20 characters.")
        exit()
        if length < 4 or length > 20:
            print("Password length should be between 4 and 20 characters.")
            exit()
use_numbers = input("Include numbers? (yes/no): ").lower()
use_symbols = input("Include symbols? (yes/no): ").lower()

characters = string.ascii_letters
if use_numbers == "yes":
    characters += string.digits

if use_symbols == "yes":
    characters += string.punctuation
elif use_symbols != "no":
    print("Invalid input for symbols. Please enter 'yes' or 'no'.")
    exit()
password = ""

for i in range(length):
    random_char = random.choice(characters)
    password += random_char

print("\nGenerated Password:")
print(password)