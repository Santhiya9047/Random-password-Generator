import random
# random------>python library
print("welcome to random password generator!")
randomchars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890!@#$%&*"
numberofpassword = int(input("Please enter the number of password to be generator"))
passwordlen = int(input("Please enter the length of the password"))

print("Here are your random password:")
for x in range(numberofpassword):
    pwd = ""
    for chars in range(passwordlen):
        pwd = pwd + random.choice(randomchars)
    print(pwd)