n = input("Enter binary number: ")
d = 0
p = 0

for i in n[::-1]:
    d += int(i) * (2 ** p)
    p += 1

print(d)