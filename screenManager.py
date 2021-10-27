from arithmetics import *
from view import *
from re import *

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
                print("-- Invalid menu selected")
                sleep(2)
        else:
            print("\n")
            spacer(15)
            print("-- Invalid menu selected")
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
                
                if (findall("[0-1]|[.]", str(biner))):
                    dec = otherToDecimal(biner, 2)
                    _, octal, hexadec = getOthersBase(dec)
                    printExclude(biner, octal, dec, hexadec, 2)
                else:
                    spacer(15)
                    print("-- !Input Error (expect 1 or 0)")
            elif menu == "2":
                spacer(15)
                octal = input("-- Enter octal number: ")
                if (findall("[0-7]|[.]", str(octal))):
                    dec = otherToDecimal(octal, 8)
                    biner, _, hexadec = getOthersBase(dec)
                    printExclude(biner, octal, dec, hexadec, 8)
                else:
                    spacer(15)
                    print("-- !Input Error (expect 0 until 7)")
            elif menu == "3":
                spacer(15)
                dec = input("-- Enter decimal number: ")
                if (findall("[0-9]|[.]", str(dec))):
                    biner, octal, hexadec = getOthersBase(dec)
                    printExclude(biner, octal, dec, hexadec, 10)
                else:
                    spacer(15)
                    print("-- !Input Error (expect 0 until 9)")
            elif menu == "4":
                spacer(15)
                hexadec = input("-- Enter hexadecimal number:")
                if (findall("[0-9]|[a-f]|[A-F]|[.]", str(hexadec))):
                    dec = otherToDecimal(hexadec, 16)
                    biner, octal, _ = getOthersBase(dec)
                    printExclude(biner, octal, dec, hexadec, 16)
                else:
                    spacer(15)
                    print("-- !Input Error (expect 0 until 9 or a|A until f|F)")
            elif menu == "0":
                mainScreen()
            elif menu == "99":
                printMenu(userHelp, 0)
            else:
                print("\n")
                spacer(15)
                print("-- Invalid menu ")
                sleep(2)
        else:
            print("\n")
            spacer(15)
            print("-- Invalid menu ")
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
    checkNum = str(num1) + str(num2)
    print("\n")
    while isAgain == "y" or isAgain == "Y":
        if str(menu) in arithChoice:
            if menu == "1":
                if (findall("[0-1]|[.]", str(checkNum))):
                    spacer(15)
                    print(">> Result : " + aritmatika(num1, num2, 2, operation))
                else:
                    spacer(15)
                    print("-- !Input Error (expect 1 or 0)")
            elif menu == "2":
                if (findall("[0-7]|[.]", str(checkNum))):
                    spacer(15)
                    print(">> Result : " + aritmatika(num1, num2, 8, operation))
                else:
                    spacer(15)
                    print("-- !Input Error (expect 0 until 7)")
            elif menu == "3":
                if (findall("[0-9]|[.]", str(checkNum))):
                    spacer(15)
                    print(">> Result : " + aritmatika(num1, num2, 10, operation))
                else:
                    spacer(15)
                    print("-- !Input Error (expect 1 until 9)")
            elif menu == "4":
                if (findall("[0-9]|[a-f]|[A-F]|[.]", str(checkNum))):
                    spacer(15)
                    print(">> Result : " + aritmatika(num1, num2, 16, operation))
                else:
                    spacer(15)
                    print("-- !Input Error (expect 0 until 7 or a|A until f|F)")
            elif menu == "0":
                mainScreen()
            elif menu == "99":
                printMenu(userHelp)
            else:
                print("\n")
                spacer(15)
                print("-- Invalid menu ")
                sleep(2)
        else:
            print("\n")
            spacer(15)
            print("-- Invalid menu ")
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