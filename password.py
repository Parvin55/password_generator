import random
import string

print("welcome to password generator")
print("***********************************")
letter=int(input("how many letters would you like to give in your password: "))
symbol=int(input("how many symbols: "))
number=int(input("how many number: "))
password_list=[]

for i in range(letter):
    l_r=str(random.choice(string.ascii_letters))
    password_list+=l_r

for i in range(symbol):
    s_r=str(random.choice(string.punctuation))
    password_list += s_r
for i in range(number):
    n_r=str(random.randint(1,9))
    password_list += n_r

# print(password_list) # simple password
random.shuffle(password_list)
# print(password_list)
password=""
for i in password_list:
    password+=i

print(password)

