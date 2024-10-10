line = input("Enter a line of text :")
words = line.split()
res = []
[res.append(x) for x in words if x not in res]
for  x in res:
    count = 0
    for i in range(0,len(words)):
        if x == words[i]:
            count += 1
    print(x,":",count)

