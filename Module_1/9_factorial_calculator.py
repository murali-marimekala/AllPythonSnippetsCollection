num = int(input("Enter a number: "))

factorial = 1

if num < 0:
    print("Factorial is not defined for a negative number")
elif num == 0:
    print("Factorial 0 is 1")
else:
    for i in range(1, num+1):
        factorial *= i
    print("Factorial of", num , "is", factorial5)