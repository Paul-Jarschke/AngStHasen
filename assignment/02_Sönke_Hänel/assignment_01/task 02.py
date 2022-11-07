### Task 02 –Reversed Words
# Write a program that reads in a word provided by the user and prints the word in a reversed order.
# For example, if the input is hello, the output should be ‘olleh’.
# a.Use a loop structure b.Use just array indexes

# a. Use a loop structure
word_input = input("Word to be reversed?\n")
word_output = ""
for char in word_input:
    word_output = char + word_output
print(word_output)

# b. Use just array indexes
word_input = input("Word to be reversed?\n")
print(word_input[::-1])
