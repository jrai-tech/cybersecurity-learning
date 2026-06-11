# Password Generator
# My first project

import random #Lets the code pick random things

print("Password: ")

#Gives random characters to choose from
characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!?@#" 

password = "" #To start with an empty password

for x in range (24): #Repeats it 24 times
    password += random.choice(characters) #Adds a random character from "characters"

print(password) #Prints the final password below "Password: "
