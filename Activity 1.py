word = input("Enter a word: ")
for i in word:
    if i == "a" or i == "A":
        print("A is found")
        break
    else:
        print("A is not found")
