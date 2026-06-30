rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))

print("Enter first matrix:")
a = []
for i in range(rows):
    row = list(map(int, input().split()))
    a.append(row)

print("Enter second matrix:")
b = []
for i in range(rows):
    row = list(map(int, input().split()))
    b.append(row)

print("Sum of matrices:")

for i in range(rows):
    for j in range(cols):
        print(a[i][j] + b[i][j], end=" ")
    print()