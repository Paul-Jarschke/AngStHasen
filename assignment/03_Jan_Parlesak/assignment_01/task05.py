# Task 05

a= int(input("Please enter side a:"))
b= int(input("Please enter side b:"))
c= int(input("Please enter side c:"))


if (c>a+b or a>c+b or b>a+c):
    print("Please enter a valid triangle")
elif(a==b and b==c):
    print("The triangle is equilateral")
elif(a==b or a==c or c==b):
    print("The triangle is an isosceles traingle")
elif(a!=c and a!=b):
    print("The triangle is scalene")