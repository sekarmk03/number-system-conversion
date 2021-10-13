from math import *
from view import *
# Using string for all bases (inc 10)

def decimalToOther(number, base) :
    output = ""
    number = int(number)
    while number > 0 :
        digit = int(number%base)

        if digit < 10 :
            output += str(digit)
        else :
            output += chr( ord('A') + (digit-10) )

        number //= base

    # output is reversed string, so output first
    return  output[::-1]

def otherToDecimal(number, base) :
    power = 1
    dec_int = 0

    number = number[::-1]

    for digit in number :
        if "0" <= digit <= "9" :
            dec_int += int(digit) * power
        else:
            dec_int += (ord(digit) - ord("A") + 10)*power
        power *= base

    return str(dec_int)

def printExclude(biner, okta, dec, hexadec, excludeBase):
    if excludeBase != 2 :
        spacer(15)
        print(">> Binary :", biner)
    if excludeBase != 8 :
        spacer(15)
        print(">> Octal :", okta)
    if excludeBase != 10 :
        spacer(15)
        print(">> Decimal :", dec)
    if excludeBase != 16 :
        spacer(15)
        print(">> Hexadecimal :", hexadec)

def getOthersBase(number) :
    return decimalToOther(number, 2), decimalToOther(number, 8), decimalToOther(number, 16)

def aritmatika(num1, num2, base, operasi):
    num1_dec = otherToDecimal(num1, base)
    num2_dec = otherToDecimal(num2, base)

    output_dec = ""
    if operasi == "+":
        output_dec = str(int(num1_dec) + int(num2_dec))
    elif operasi == "-":
        output_dec = str(int(num1_dec) - int(num2_dec))
    elif operasi == "x" or operasi == "*":
        output_dec = str(int(num1_dec) * int(num2_dec))
    elif operasi == ":" or operasi == "/":
        output_dec = str(int(num1_dec) / int(num2_dec))

    output = decimalToOther(output_dec, base)
    return output