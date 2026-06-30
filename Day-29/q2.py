arr = list(map(int, input("Enter array elements: ").split()))

print("1. Display")
print("2. Sum")
print("3. Maximum")

choice = int(input("Enter your choice: "))

if choice == 1:
    print(arr)

elif choice == 2:
    print("Sum =", sum(arr))

elif choice == 3:
    print("Maximum =", max(arr))

else:
    print("Invalid Choice")