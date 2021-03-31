import random

print("Welcome to the Password Generator!!!")

num_letters = int(input("\nHow many letters would you like in your password? "))
num_symbols = int(input("How many symbols would you like? "))
num_numbers = int(input("How many numbers would you like? "))

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '/', '?', ',', '<', '>']

password = ""

for letter in range(num_letters):
    password += letters[random.randint(0, len(letters) - 1)]

for symbol in range(num_symbols):
    password += symbols[random.randint(0, len(symbols) - 1)]

for number in range(num_numbers):
    password += numbers[random.randint(0, len(numbers) - 1)]

final_password = ''.join(random.sample(password, len(password)))

print(f"\nHere is your password: {final_password}")