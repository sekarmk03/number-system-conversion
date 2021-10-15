from math import *
from view import *
# Using string for all bases (inc 10)

def decimalToOther(number, base) :
    whole = ""
    floating = "."
    digit = 0
    if "." in number:
        number, frac = number.split(".")
        frac = float("0." + frac)
        while frac != 1.0:
            frac -= int(digit)
            digit = frac * base
            if digit < 10:
                floating += str(int(digit))
            else:
                floating += chr(ord('A') + (int(digit) - 10))
            frac *= base
            if digit == 0:
                frac = 1.0

    number = int(float(number))
    while number > 0 :
        digit = int(number % base)

        if digit < 10 :
            whole += str(digit)
        else :
            whole += chr( ord('A') + (digit-10) )

        number //= base

    # whole is reversed string
    return (whole[::-1] + floating) if floating != "." else (whole[::-1])

def otherToDecimal(number, base) :
    power = 1
    dec_int = 0
    floating = 0

    if "." in str(number):
        number, fract = str(number).split(".")
        for idx, digit in enumerate(fract):
            floating += int(digit)*base**(-(idx+1))

    number = number[::-1]

    for digit in number :
        if "0" <= digit <= "9" :
            dec_int += int(digit) * power
        else:
            dec_int += (ord(digit) - ord("A") + 10)*power
        power *= base

    return str(dec_int + floating)

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
        output_dec = str(float(num1_dec) + float(num2_dec))
    elif operasi == "-":
        output_dec = str(float(num1_dec) - float(num2_dec))
    elif operasi == "x" or operasi == "*":
        output_dec = str(float(num1_dec) * float(num2_dec))
    elif operasi == ":" or operasi == "/":
        output_dec = str(float(num1_dec) / float(num2_dec))

    output = str(decimalToOther(output_dec, base))
    return str(output)