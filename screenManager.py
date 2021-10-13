from arithmetics import *
from view import *

def mainScreen():
    printMenu(mainMenu, len(mainChoice))
    menu = choosenMenu()
    while True:
        if str(menu) in mainChoice:
            match menu:
                case "1":
                    numScreen()
                case "2":
                    arithScreen()
                case "0":
                    return
                case "99":
                    print("help")
                case "88":
                    print("about")
                case _:
                    print("\n")
                    spacer(15)
                    print("-- Menu yg dipilih tidak valid")
                    sleep(2)
        else:
            print("\n")
            spacer(15)
            print("-- Menu yg dipilih tidak valid")
            sleep(2)
        printMenu(mainMenu, len(mainChoice))
        menu = choosenMenu()

def numScreen():
    printMenu(numConvMenu, len(numChoice))
    menu = choosenMenu()
    isAgain = "y"
    while (isAgain == "y" or isAgain == "Y") and menu != 0:
        if str(menu) in numChoice:
            match menu:
                case "1":
                    spacer(15)
                    biner = input("-- Enter binary number: ")
                    dec = otherToDecimal(biner, 2)
                    _, okta, hexadec = getOthersBase(dec)
                    printExclude(biner, okta, dec, hexadec, 2)
                case "2":
                    spacer(15)
                    okta = input("-- Enter octal number: ")
                    dec = otherToDecimal(okta, 8)
                    biner, _, hexadec = getOthersBase(dec)
                    printExclude(biner, okta, dec, hexadec, 8)
                case "3":
                    spacer(15)
                    dec = input("-- Enter decimal number: ")
                    biner, okta, hexadec = getOthersBase(dec)
                    printExclude(biner, okta, dec, hexadec, 10)
                case "4":
                    spacer(15)
                    hexadec = input("-- Enter hexadecimal number:")
                    dec = otherToDecimal(hexadec, 16)
                    biner, okta, _ = getOthersBase(dec)
                    printExclude(biner, okta, dec, hexadec, 16)
                case "0":
                    mainScreen()
                case "99":
                    print("help")
                case _:
                    print("\n")
                    spacer(15)
                    print("-- Menu yg dipilih tidak valid")
                    sleep(2)
        else:
            print("\n")
            spacer(15)
            print("-- Menu yg dipilih tidak valid")
            sleep(2)
        isAgain = cycleCont()
        if isAgain == "y" or isAgain == "Y":
            printMenu(numConvMenu, len(numChoice))
            menu = choosenMenu()
    mainScreen()

def arithScreen():
    printMenu(arithMenu, len(arithChoice))
    menu = choosenMenu()
    isAgain = "y"
    print("\n")
    spacer(15)
    num1 = input("-> Enter first number : ")
    spacer(15)
    operation = input("-> Operation (+,-,/,*) : ")
    spacer(15)
    num2 = input("-> Enter second number : ")
    print("\n")
    while isAgain == "y" or isAgain == "Y":
        if str(menu) in arithChoice:
            match menu:
                case "1":
                    spacer(15)
                    print(">> Hasil : " + aritmatika(num1, num2, 2, operation))
                case "2":
                    spacer(15)
                    print(">> Hasil : " + aritmatika(num1, num2, 8, operation))
                case "3":
                    spacer(15)
                    print(">> Hasil : " + aritmatika(num1, num2, 10, operation))
                case "4":
                    spacer(15)
                    print(">> Hasil : " + aritmatika(num1, num2, 16, operation))
                case "0":
                    mainScreen()
                case "99":
                    print("help")
                case _:
                    print("\n")
                    spacer(15)
                    print("-- Menu yg dipilih tidak valid")
                    sleep(2)
        else:
            print("\n")
            spacer(15)
            print("-- Menu yg dipilih tidak valid")
            sleep(2)
        isAgain = cycleCont()
        if isAgain == "y" or isAgain == "Y":
            printMenu(arithMenu, len(arithChoice))
            menu = choosenMenu()
            print("\n")
            spacer(15)
            num1 = input("-> Enter first number : ")
            spacer(15)
            operation = input("-> Operation (+,-,/,*) : ")
            spacer(15)
            num2 = input("-> Enter second number : ")
            print("\n")
    mainScreen()

def goodByeScreen(name):
    clearScreen()
    byeStr = [
        "Thank you for using our app!",
        "We hope you enjoyed it!",
        "See you next time, " + name + "!",
        "",
        "Please wait...",
        "App will be closed in "
    ]
    printRunningText(byeStr, 15)

    for i in range(3):
        clearScreen()
        for j in range(len(byeStr)):
            if j < len(byeStr) - 1:
                spacer(15)
                print(byeStr[j])
            else:
                spacer(15)
                print(byeStr[j], end="")
        print(3 - i)
        sleep(1)