words = input("Enter words: ").split()

words.sort(key=len)

print("Words sorted by length:")

for word in words:
    print(word)