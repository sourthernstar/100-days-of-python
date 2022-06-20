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

new_pswd=[]
counts=nr_letters+nr_symbols+nr_numbers

for i in range(nr_letters):
  choice=random.randint(0,len(letters)-1)
  new_pswd.append(letters[choice])

for i in range(nr_symbols):
  choice=random.randint(0,len(symbols)-1)
  new_pswd.append(symbols[choice])
  
for i in range(nr_numbers):
  choice=random.randint(0,len(numbers)-1)
  new_pswd.append(numbers[choice])

print(''.join(new_pswd))

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

random_new_pswd=[]
for i in range(counts):
  choice=random.randint(0,len(new_pswd)-1)
  random_new_pswd.append(new_pswd[choice])
  new_pswd.remove(new_pswd[choice])

print(''.join(random_new_pswd))