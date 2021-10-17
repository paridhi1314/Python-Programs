l = []
n = int(input("Enter the n"))
for i in range(n):
    v = int(input("Enter number = "))
    l.append(v)

largest = l[0]
for i in range(n):
    if l[i]>largest:
        largest = l[i]

second_largest = l[0]
for i in range(n):
    if l[i]>second_largest:
        if largest!=l[i]:
            second_largest = l[i]


print("The second largest is ",second_largest)