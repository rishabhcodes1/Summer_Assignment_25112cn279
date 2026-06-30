
arr = [10, 20, 30, 20, 40, 10]

duplicates = []

for num in arr:
    if arr.count(num) > 1 and num not in duplicates:
        duplicates.append(num)

print("Duplicate elements:", duplicates)