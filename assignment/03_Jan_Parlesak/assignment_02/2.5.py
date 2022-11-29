user_input= input("Enter an expression:")
new_character='.'
count=0

for i in range(0,len(user_input)):
    if i>len(user_input):
        break
    if count<0:
        break
    if user_input[i]=="(":
        count= count +1
        for j in range(0,len(user_input[i:])):
            if user_input[i:][j]==")":
                count=count-1
                user_input=user_input[0:(j+i):]+ new_character +user_input[(j+i+1)::]
                print(user_input)
                break
    if user_input[i]==")":
        count=count-1
    else:
        continue

if count==0:
    print("correct")
else:
    print("incorrect")