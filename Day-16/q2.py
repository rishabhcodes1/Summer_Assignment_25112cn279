
arr = list(map(int, input("Enter elements: ").split()))

max_count = 0
element = arr[0]

for i in arr:
    count = arr.count(i)
    if count > max_count:
        max_count = count
        element = i

print("Element:", element)
print("Frequency:", max_count)