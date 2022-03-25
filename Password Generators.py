from random import *
from string import *
import os

# creating stirng values in variables using 'string' library.
symbols = "!@#$%^&*()"
upper, lower, number = ascii_uppercase, ascii_lowercase, digits
all_char = upper + lower + number + symbols
history = []


def clear():
    os.system("cls" if os.name == "nt" else "clear")

# generate passoword as many as user wants.
def generate_all():
    length = int(input("Input password length: "))
    many = int(input("How many password do you want:"))
    clear()
    counter = 0

    while counter < many:
        counter += 1
        password = ""
        for _ in range(length):
            password += choice(all_char)
        print("Your password {} :{}".format(counter, password))
        history.append(password)


def gen_onlynum_letter():
    length = int(input("Input password length: "))
    many = int(input("How many password do you want:"))
    clear()
    counter = 0

    while counter < many:
        counter += 1
        password = ""
        for _ in range(length):
            password += choice(ascii_letters+number)
        print("Your password {} :{}".format(counter, password))
        history.append(password)

# user custom password generator fucntion.
def custom():
    char = str(input("Input your custom charachters all at once: "))
    length = int(input("Input password length: "))
    many = int(input("How many password do you want: "))
    clear()
    counter = 0

    while counter < many:
        counter += 1
        password = ""

        for _ in range(length):
            password += choice(char)
        print("Your password {} :{}".format(counter, password))
        history.append(password)


def show_help():
    print("Type '1' to create password with lower/upper case letter +number + symbols.")
    print("TYpe '2' to create password with without symbols.")
    print("Type '3' to create passowrd with your custom prefrences.\n")
    print("Type '/history' to see your created password collection.")

# program loop

def start():
    while 1:
        print("Type '/help to see help menu' or 'quit' to exit\n")
        user = input("> ").lower()

        if user == 'quit':
            break

        elif user == '1':
            clear()
            generate_all()
        elif user == '2':
            clear()
            gen_onlynum_letter()
        elif user == '3':
            clear()
            custom()
        elif user == '/history':
            clear()
            print(history)
        elif user == '/help':
            clear()
            show_help()

# functions invoker:
show_help()
start()
print('Thanks for using password generator')
# made by Poya
