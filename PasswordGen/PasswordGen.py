#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91


#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

random_symbols = random.randint(0,len(symbols))
random_number = random.randint(0,len(numbers))

password = ''


for i in range(nr_letters):
    random_letter = random.randint(0, len(letters) - 1)
    password += letters[random_letter]

for i in range(nr_numbers):
    random_number = random.randint(0, len(numbers) - 1)
    password += numbers[random_number]

for i in range(nr_symbols):
    random_symbols = random.randint(0, len(symbols) - 1)
    password += symbols[random_symbols]

# Convert password string to list
password_list = list(password)

# Shuffle the password list in place
random.shuffle(password_list)

# Convert the shuffled list back to a string
shuffled_password = ''.join(password_list)

print(shuffled_password)