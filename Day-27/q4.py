name = input("Enter student name: ")

m1 = int(input("Enter marks of Subject 1: "))
m2 = int(input("Enter marks of Subject 2: "))
m3 = int(input("Enter marks of Subject 3: "))

total = m1 + m2 + m3
percentage = total / 3

print("\nResult")
print("Name :", name)
print("Total Marks :", total)
print("Percentage :", percentage)

if percentage >= 40:
    print("Result : Pass")
else:
    print("Result : Fail")