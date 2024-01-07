import random
import string

characters = list(string.ascii_letters + string.digits + "!@#$%^&*()")

def generate_password():
    # Define character sets
    length = int(input("Enter the desired length of your password:"))
   
    random.shuffle(characters)

    password = []

    for x in range(length):
        password.append(random.choice(characters))

    random.shuffle(password)

    password = "".join(password)
    print(password)

option = input("Do you want to generate a password? Enter (Yes or No):")

if option == "Yes":
    generate_password()
elif option == "No":
    print("Goodbye!")
    quit()
else:
    print("Invalid input")
    quit()