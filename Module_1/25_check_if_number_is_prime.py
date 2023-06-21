n = int(input("Enter a number: "))

is_prime = True
for num in range(2, int(n ** 0.5) + 1):
    if n % num == 0:
        is_prime = False
        break
if is_prime and n > 1:
    print(n, "is a prime number ")
else:
    print(n, "is not a prime number")