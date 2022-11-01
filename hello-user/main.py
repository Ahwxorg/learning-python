# Import modules
import os

# Greeting
greeting = "Hey"

# Get username
user = os.getlogin()

print(greeting + ", " + user)


# Now the actual assignment
nick = input("Please enter your nickname: ")

print("Hello, " + nick)
