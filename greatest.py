a = int(input("Enter the number"))
b = int(input("Enter the sec number"))
c = int(input("Enter the third number"))

if(a>b):
    if(a>c):
        print(a, " is greatest")
    else:
        print(c, " is greatest")
elif(b>c):
    if(b>a):
        print(b, " is greatest")
    else:
        print(a, " is greatest")

else:
    print(c, " is greatest")





