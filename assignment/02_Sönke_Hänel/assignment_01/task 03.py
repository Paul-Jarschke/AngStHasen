### Task 03 –Fibonacci Numbers
# Write a program that reads in an upper bound (number) provided by the user and
# prints the sequence of Fibonacci numbers that are less or equal to the number given by the user.
# Use a while-loop for this task.The Fibonacci sequence is defined as 𝐹𝑛=𝐹𝑛−1+𝐹𝑛−2.
# Use 𝐹0=0 and 𝐹1=1 as seed values. For example, if the user inputs 6, the output should be 0, 1, 1, 2, 3, 5.

# input reception
input_fib = int(input("Provide an upper bound (number) please.\n"))

f_0 = 0
f_1 = 1

print(f_0)
while (f_1 <= input_fib):
    print(f_1)
    temp = f_1
    f_1 = f_1 + f_0
    f_0 = temp
