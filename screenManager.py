from arithmetics import *
from view import *

def mainScreen():
    printMenu(mainMenu, len(mainMenu)-1)
    menu = choosenMenu()
    isAgain = 'y'
    while isAgain == 'y' or isAgain == 'Y':
        if str(menu) in mainChoice:
            if menu == "1":
                numScreen()
            elif menu == "2":
                arithScreen()
            elif menu == "0":
                return
            elif menu == "99":
                printMenu(userHelp, 0)
                isAgain = cycleCont()
            elif menu == "88":
                printMenu(aboutApp, 0)
                isAgain = cycleCont()
            else:
                print("\n")
                spacer(15)
                print("-- Menu yg dipilih tidak valid")
                sleep(2)
        else:
            print("\n")
            spacer(15)
            print("-- Menu yg dipilih tidak valid")
            sleep(2)
        if isAgain == 'y' or isAgain == 'Y':
            printMenu(mainMenu, len(mainMenu)-1)
            menu = choosenMenu()
        else:
            return

def numScreen():
    printMenu(numConvMenu, len(numConvMenu)-1)
    menu = choosenMenu()
    isAgain = "y"
    while (isAgain == "y" or isAgain == "Y") and menu != 0:
        if str(menu) in numChoice:
            if menu == "1":
                spacer(15)
                biner = input("-- Enter binary number: ")
                dec = otherToDecimal(biner, 2)
                _, okta, hexadec = getOthersBase(dec)
                printExclude(biner, okta, dec, hexadec, 2)
            elif menu == "2":
                spacer(15)
                okta = input("-- Enter octal number: ")
                dec = otherToDecimal(okta, 8)
                biner, _, hexadec = getOthersBase(dec)
                printExclude(biner, okta, dec, hexadec, 8)
            elif menu == "3":
                spacer(15)
                dec = input("-- Enter decimal number: ")
                biner, okta, hexadec = getOthersBase(dec)
                printExclude(biner, okta, dec, hexadec, 10)
            elif menu == "4":
                spacer(15)
                hexadec = input("-- Enter hexadecimal number:")
                dec = otherToDecimal(hexadec, 16)
                biner, okta, _ = getOthersBase(dec)
                printExclude(biner, okta, dec, hexadec, 16)
            elif menu == "0":
                mainScreen()
            elif menu == "99":
                printMenu(userHelp, 0)
            else:
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
            printMenu(numConvMenu, len(numConvMenu)-1)
            menu = choosenMenu()
    mainScreen()

def arithScreen():
    printMenu(arithMenu, len(arithMenu)-1)
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
            if menu == "1":
                spacer(15)
                print(">> Hasil : " + aritmatika(num1, num2, 2, operation))
            elif menu == "2":
                spacer(15)
                print(">> Hasil : " + aritmatika(num1, num2, 8, operation))
            elif menu == "3":
                spacer(15)
                print(">> Hasil : " + aritmatika(num1, num2, 10, operation))
            elif menu == "4":
                spacer(15)
                print(">> Hasil : " + aritmatika(num1, num2, 16, operation))
            elif menu == "0":
                mainScreen()
            elif menu == "99":
                printMenu(userHelp)
            else:
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
            printMenu(arithMenu, len(arithMenu)-1)
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