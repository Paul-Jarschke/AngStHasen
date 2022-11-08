# Task 03

Number = int(input("Please enter a number:"))
F_zero = 0
F_one = 1
Fib = 0

while F_zero <= Number:
    print(F_zero)
    if (F_one > Number):
        break
    print(F_one)
    F_zero = F_one + F_zero
    F_one = F_zero + F_one