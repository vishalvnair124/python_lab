a = input("Enter the first Number  : ")
b = input("Enter the Second Number : ")
c = input("Enter the Third Number  : ")

if a > b :
    if a > c :
        print("The largest number is ", a)
    else :
        print("The largest number is ", c)
else:
    if b > c :
        print("The largest number is ", b)
    else :
        print("The largest number is ", c)