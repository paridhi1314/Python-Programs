l = []
n = int(input("Enter N = "))
for i in range(n):
    v = int(input("Enter number = "))
    l.append(v)

small = l[0]
if i in range(n):
    if small>l[i]:
        small = l[i]

second_smallest = l[0]
if i in range(n):
    if second_smallest>l[i]:
        if small!=l[i]:
            second_smallest = l[i]



print("The second amallest element is ", second_smallest);
#
# lis = [1,45,12,56,89,90,67,34]
# lis.sort()
# print(lis[1])
# print(lis[-2])


