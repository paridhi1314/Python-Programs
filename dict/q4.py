dic = {10:'A',20:'B',30:'C',40:'D'}
n = int(input("Which key you want to check?"))
for key in dic:
    if key == n:
        print(n," is present in dictionary")
        break
else:
    print(n , " is not a key")