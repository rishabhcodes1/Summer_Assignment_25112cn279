balance = 5000

print("1. Check Balance")
print("2. Withdraw")

choice = int(input("Enter choice: "))

if choice == 1:
    print("Balance =", balance)

elif choice == 2:
    amount = int(input("Enter amount: "))

    if amount <= balance:
        balance = balance - amount
        print("Withdraw Successful")
        print("Balance =", balance)
    else:
        print("Insufficient Balance")

else:
    print("Invalid Choice")