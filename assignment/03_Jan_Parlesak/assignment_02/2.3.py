newdict= {}

string_input = input("Please enter a string:")
string_input= string_input.replace(' ','')
letters=  string_input.strip()

for letter in letters:
    newdict[letter]= newdict.get(letter,0)+1

print(newdict)