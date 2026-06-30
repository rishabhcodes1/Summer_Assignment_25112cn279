
text = input("Enter a string: ")

for ch in sorted(set(text)):
    if ch != " ":
        print(ch, "=", text.count(ch))