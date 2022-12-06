
queue= []
add=input("do you want to add? y/n")
if add=="n":
    print("WHY?")
while(add=="y"):
        name=input("Please enter the name:")
        queue.append(name)
        add=input("add a name? y/n")

i=0
while(i < len(queue)):
    input("Press Enter for next in queue")
    print(queue[i])
    i=i+1
print("End of queue")




