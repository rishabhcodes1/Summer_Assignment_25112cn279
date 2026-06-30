num = int(input("Enter a number: "))
s = 0

for i in range(1, num):
    if num % i == 0:
        s += i

if s == num:
    print(num, "is a Perfect Number")
else:
    print(num, "is not a Perfect Number")