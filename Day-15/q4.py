arr = [1, 0, 2, 0, 3, 0, 4]

result = []

for num in arr:
    if num != 0:
        result.append(num)

zero_count = arr.count(0)

for i in range(zero_count):
    result.append(0)

print("Result =", result)