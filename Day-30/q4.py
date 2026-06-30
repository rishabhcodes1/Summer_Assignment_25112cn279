def display_result(name, marks):

    total = sum(marks)
    percentage = total / len(marks)

    print("\nStudent Name :", name)
    print("Total Marks :", total)
    print("Percentage :", percentage)

name = input("Enter student name: ")

marks = list(map(int, input("Enter 3 marks: ").split()))

display_result(name, marks)