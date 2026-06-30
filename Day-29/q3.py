text = input("Enter a string: ")

print("1. Uppercase")
print("2. Lowercase")
print("3. Reverse")

choice = int(input("Enter your choice: "))

if choice == 1:
    print(text.upper())

elif choice == 2:
    print(text.lower())

elif choice == 3:
    print(text[::-1])

else:
    print("Invalid Choice")