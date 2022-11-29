import random

random_list=[]

for i in range(0,30):
    n = random.randint(1, 100)
    random_list.append(n)

it= iter(random_list)

random_list= zip(it,it,it)

print(random_list)

sorted_data= sorted(random_list, key=lambda tup:tup[2])
print(sorted_data)
