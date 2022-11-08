#Task 06

Number = float(input("Please enter a number:"))
octal = 0
count = 1
Quotient = 1
if Number < 0:
    print("Please enter a valid number")
else:
    Number = Number * (8 ** (16))
    while Quotient > 0:
        remainder = Number % 8
        Quotient = Number // 8
        Number = Quotient
        octal = octal + remainder * count
        count = count * 10
    print(octal / 10 ** 16)
