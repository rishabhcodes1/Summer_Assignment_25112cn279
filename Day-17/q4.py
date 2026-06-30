arr1 = list(map(int, input("Enter first array: ").split()))
arr2 = list(map(int, input("Enter second array: ").split()))

print("Common Elements:")

for i in arr1:
    if i in arr2:
        print(i, end=" ")