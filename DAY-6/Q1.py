n = int(input("Enter decimal number: "))
b = ""

while n > 0:
    b = str(n % 2) + b
    n //= 2

print(b)