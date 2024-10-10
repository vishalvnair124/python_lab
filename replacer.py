word = input("Enter a word :")
firstChar = word[0]
for i in range(0,len(word)):
    if i == 0 :
        print(word[i],end="")
    elif  word[i] == firstChar:
        print('$',end="")
    else :
        print(word[i],end="")
  