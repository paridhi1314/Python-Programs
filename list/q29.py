l = []
n = int(input("Enter the n"))
for i in range(n):
    v = int(input("Enter number = "))
    l.append(v)

print("The original list is : ",l)

my_set = set(l)
my_new_list = list(my_set)
print("List of unique elements ",my_new_list)
