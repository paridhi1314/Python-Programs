dic = {'a':10,'b':20,'c':30}
product = 1
for i in dic:
    values = dic.get(i)
    product *= values


print(product)
