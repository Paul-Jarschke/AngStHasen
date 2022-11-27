# Task 02
# Write a program that reads in a word provided by the user and prints the word in a reversed order.
# For example, if the input is hello, the output should be ‘olleh’.

# Using a loop structure
print('Which word would you like to reverse?')
word_a = input()

reverse_a = ''
for i in word_a:
    reverse_a = i + reverse_a

print(f'The reversed order of your word is : {reverse_a}')

# Using just array index
print('Which word would you like to reverse?')
word_b = input()

reverse_b = word_b[::-1]

print(f'The reversed order of your word is : {reverse_b}')
