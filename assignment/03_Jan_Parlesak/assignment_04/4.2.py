
s="Hello, how is it going?"
n=3



def  remove_long_words(s,n):
    sentence=s.split()
    comp= [word for word in sentence if len(word)<=n]
    print(comp)

remove_long_words(s,n)

