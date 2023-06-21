n = int(input("Enter the number of terms: "))

a, b = 0, 1
count = 0

if n <= 0:
    print("Please enter a postive number")
elif n == 1:
    print("Fibanacci series: ")
    print(a)
else:
    print("Fibanacci serias: ")
    while count <= n:
        print(a, end=" ")
        nth = a + b
        a = b
        b = nth
        count += 1