import random
random_list=[]

for i in range(0,10):
    n= random.randint(1,100)
    random_list.append(n)

print(random_list)

largest_int=0
for i in random_list:
    if(i>largest_int):
        largest_int= i
    else:
        continue

print(largest_int)