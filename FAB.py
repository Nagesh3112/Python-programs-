num = int(input("Enter a number: "))

if num % 2 == 0:
    print("Even number")
else:
    print("Not an even number")

my_list = [10, 20, 30, 40, 50]

for x in my_list:
    print(x)

0
total = 0

for n in range(2, 200):
    prime = True

    for i in range(2, n):
        if n % i == 0:
            prime = False
            break

    if prime:
        total = total + n

print("Sum of primes below 200 =", total)
a = 1
b = 2

for i in range(10):
    print(a)
    c = a + b
    a = b
    b = c
