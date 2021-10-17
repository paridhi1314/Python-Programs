dic = {}
n = int(input("enter the number "))

for i in range(1,n+1):
    dic.update({i:i*i})

print(dic)