#Fizzbuzz program

def fizzbuzz(n):
    for i in range(1, n+1):
        if i % 3 == 0 and i % 5 == 5:
            print("Fizzbuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:   
            print(i)
n = int(input("Enter number for fizzbuzz: "))
fizzbuzz(n) 