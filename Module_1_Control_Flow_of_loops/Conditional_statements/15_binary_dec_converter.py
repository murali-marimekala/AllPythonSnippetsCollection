#Title: Convert a binary number to decimal number

binary = input("Enter a binary number: ")

decimal = 0

for digit in binary:
    decimal = decimal * 2 + int(digit)

print("Decimal representation : ", decimal)