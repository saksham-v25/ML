import random

letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J',
           'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
           'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbol = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')']

print("welcome to the world of passwprd genrator ")
n_letters = int(input("How many letters you want in the password :"))
n_numbers = int(input("How many  the number you wnat in password:"))
n_symbol = int(input("How many symbol you want in password : "))

password_list = []
for i in range(1,n_letters+1) :
    char = random.choice(letters)
    password_list += char

print(password_list)

for i in range(1,n_numbers+1) :
    char = random.choice(numbers)
    password_list += char
print(password_list)

for i in range(1,n_symbol+1):
        char = random.choice(symbol)
        password_list += char
print(password_list)

random.shuffle(password_list)
print( password_list)

password = ''
for i in password_list :
    password= password +i
print(password)