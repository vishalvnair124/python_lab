word = input("Enter a word :")
for i in range(0,len(word)):
    if i == 0 :
        print(word[len(word)-1],end="")
    elif  i == len(word)-1 :
        print(word[0],end="")
    else :
        print(word[i],end="")