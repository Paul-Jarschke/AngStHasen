import numpy as np

numbers = np.random.randint(1,100,20)

x= lambda a: True if a%2==0 else False

new_array=[]
for number in numbers:
    if x(number):
        new_array.append(number)
    else:
        continue

print(numbers)
print(new_array)

