l1 = [1,34,56,78,89]
l2 = [89,45,67,88,66]

diff = list(set(l2)-set(l1))
diff2 = list(set(l1)-set(l2))

total_diff = diff+diff2;
print(total_diff)