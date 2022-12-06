expression=input("Enter an expression:")

def check(icon_open,icon_close, user_input):
    new_character = '.'
    count = 0

    for i in range(0, len(user_input)):
        if i > len(user_input):
            break
        if count < 0:
            break
        if user_input[i] == icon_open:
            count = count + 1
            for j in range(0, len(user_input[i:])):
                if user_input[i:][j] == ")" or "]" or "}" and user_input!=icon_close:
                    return 0
                if user_input[i:][j] == icon_close:
                    count = count - 1
                    user_input = user_input[0:(j + i):] + new_character + user_input[(j + i + 1)::]
                    break
        if user_input[i] == icon_close:
            count = count - 1
        else:
            continue

    if count == 0:
        return 1
    else:
        return 0


for i in range(len(expression)):
    if expression[i]=="(":
        open="("
        close=")"
        if(check(open,close,expression)==1):
            print("correct ()")
        if(check(open,close,expression)==0):
            print("incorrect ()")

    if expression[i]=="[":
        open="["
        close="]"
        if (check(open, close, expression) == 1):
            print("correct []")
        if (check(open, close, expression) == 0):
            print("incorrect []")
    if expression[i]=="{":
        open="{"
        close="}"
        if (check(open, close, expression) == 1):
            print("correct {}")
        if (check(open, close, expression) == 0):
            print("incorrect {}")