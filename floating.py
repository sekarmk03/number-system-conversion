"""
def float_bin(number, places = 3):
	whole, dec = str(number).split(".")
	whole = int(whole)
	dec = int (dec)
	res = bin(whole).lstrip("0b") + "."
	for x in range(places):
		whole, dec = str((decimal_converter(dec)) * 2).split(".")
		dec = int(dec)
		res += whole
	return res

def decimal_converter(num):
	while num > 1:
		num /= 10
	return num

n = input("Enter your floating point value : \n")
p = int(input("Enter the number of decimal places of the result : \n"))

print(float_bin(n, places = p))

def float_octal(number, places = 3):
	whole, dec = str(number).split(".")
	whole = int(whole)
	dec = int (dec)
	res = oct(whole).lstrip("0o") + "."
	for x in range(places):
		whole, dec = str((decimal_converter(dec)) * 8).split(".")
		dec = int(dec)
		res += whole
	return res
"""
def main():
    number = "268.625"
    base = 16
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
    print(whole[::-1] + floating)

if __name__ == "__main__" :
    main()