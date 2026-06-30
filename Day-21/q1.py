rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))

matrix = []

print("Enter matrix:")

for i in range(rows):
    row = list(map(int, input().split()))
    matrix.append(row)

print("Column-wise Sum:")

for j in range(cols):
    total = 0
    for i in range(rows):
        total = total + matrix[i][j]
    print("Column", j + 1, "=", total)