
rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))

matrix = []

print("Enter matrix:")

for i in range(rows):
    row = list(map(int, input().split()))
    matrix.append(row)

print("Row-wise Sum:")

for i in range(rows):
    total = sum(matrix[i])
    print("Row", i + 1, "=", total)