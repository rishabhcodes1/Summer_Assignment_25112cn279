def is_palindrome(n):
    original = str(n)
    reverse = original[::-1]

    return original == reverse

num = int(input("Enter a number: "))

if is_palindrome(num):
    print("Palindrome Number")
else:
    print("Not a Palindrome Number")