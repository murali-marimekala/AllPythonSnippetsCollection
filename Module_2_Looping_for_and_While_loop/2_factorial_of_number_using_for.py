n = int(input("Enter a number: "))
factorial = 1

for num in range(1, n+1):
    factorial *= num

print("The factorial of ", n, " is ", factorial)