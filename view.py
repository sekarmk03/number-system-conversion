from os import *
from subprocess import *
from time import *
from re import *
from arithmetics import *
# Using string for all bases (inc 10)

def clearScreen():
    # for windows
    if name == 'nt':
        _ = system('cls')
  
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')

def spacer(n):
    print(" " * n, end="")

def printRunningText(text, spacing):
    for i in range(len(text)):
        spacer(spacing)
        for j in range(len(text[i])):
            print(text[i][j], end="")
            sleep(0.05)
        print("")

def welcomeScreen():
    clearScreen()
    helloStr = [
        "Welcome to Our Application!",
        "We will help you solve problems of number system conversions",
        "and arithmetic operations.",
        "Enjoy!"
    ]
    printRunningText(helloStr, 15)
    spacer(15)
    name = input("Enter your name : ")
    clearScreen()
    helloName = [
        "Hello, " + name + "!\n",
        "Please wait...",
        "Redirecting in "
    ]
    printRunningText(helloName, 15)
    for i in range(3):
        clearScreen()
        spacer(15)
        print(helloName[0])
        spacer(15)
        print(helloName[1])
        spacer(15)
        print(helloName[2], end="")
        print(3 - i)
        sleep(1)
    return name

def printMenu(listMenu, n):
    clearScreen()
    appHeader()
    for i in range(n):
        spacer(15)
        print(listMenu[0])
        spacer(15)
        print(listMenu[i + 1])
    spacer(15)
    print(listMenu[0])

# header app
def appHeader():
    header = [
        "++============================++",
        "::    Number Conversion App   ::",
        "::       - by Team 5 -        ::",
        "++============================++"
    ]
    for i in range(len(header)):
        spacer(15)
        print(header[i])

# cycle controller
def cycleCont():
    spacer(15)
    isAgain = input("-- Wanna try once again? (y/n) ")
    return isAgain

def choosenMenu():
    spacer(15)
    return input("-- Enter your choice : ")

def listingMenu(menuList):
    dec = []
    for i in range(len(menuList)):
        dec += findall(r"[-+]?\d*\.\d+|\d+", menuList[i])
    return dec

# menu
mainMenu = [
    "+------------------------------+",
    "|          Main Menu           |",
    "| 1. Number Conversion         |",
    "| 2. Arithmetics Operation     |",
    "| 0. Exit                      |",
    "| 99. Help                     |",
    "| 88. About                    |"
]
mainChoice = listingMenu(mainMenu)

numConvMenu = [
    "+------------------------------+",
    "|       Number Conversion      |",
    "| 1. Biner                     |",
    "| 2. Octal                     |",
    "| 3. Decimal                   |",
    "| 4. Hexadecimal               |",
    "| 0. Back to main menu         |",
    "| 99. Help                     |"
]
numChoice = listingMenu(numConvMenu)

arithMenu = [
    "+------------------------------+",
    "|     Arithmetic Operation     |",
    "| 1. Biner                     |",
    "| 2. Octal                     |",
    "| 3. Decimal                   |",
    "| 4. Hexadecimal               |",
    "| 0. Back to main menu         |",
    "| 99. Help                     |"
]
arithChoice = listingMenu(arithMenu)
