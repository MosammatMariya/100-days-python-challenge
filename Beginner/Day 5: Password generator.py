import random

letters=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
numbers=['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
symbols=['!', '#', '$', '%', '&', '*', '+']

print("Welcome to PyPassword generator")
letter=int(input("How many letters you want in your password?\n"))
symbol=int(input("How many symbols you want in your password?\n"))
number=int(input("How many numbers you want in your password?\n"))

password=[]
for char in range(0, letter):
    password.extend(random.choice(letters))

for char in range(0, symbol):
    password.append(random.choice(symbols))

for char in range(0, number):
    password.append(random.choice(numbers))
print(password) #before suffle

random.shuffle(password)
print(password) #after suffle
#turning list into strings
p=""
for char in password:
    p+=char
print("Your password: ",p)
