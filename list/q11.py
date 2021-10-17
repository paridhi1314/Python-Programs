l1 = [1,2,3,4,5]
l2 = [5,6,7,3,9]
count = 0

for i in l1:
    for j in l2:
        if(i == j):
            count = count + 1;

print(count)