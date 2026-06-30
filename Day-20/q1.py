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

result = []

for i in range(rows):
    temp = []
    for j in range(cols):
        sum = 0
        for k in range(cols):
            sum = sum + a[i][k] * b[k][j]
        temp.append(sum)
    result.append(temp)

print("Matrix Multiplication:")

for row in result:
    print(row)