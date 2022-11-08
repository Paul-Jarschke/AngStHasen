# Task 02

Word = list(input("Please enter a word:"))
count = len(Word) - 1
backwards = list()

while count >= 0:
    backwards.append(Word[count])
    count = count - 1
print("".join(backwards))
