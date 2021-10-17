

from array import *
arr = array('i',[])
length = int(input("Enter the length of array: "))
for i in range(length):
  x = int(input("Enter the next value: "))
  arr.append(x)
print(arr)
val = int(input("Enter the number you want to delete:"))
k = 0
for e in arr:
  if e ==val:
    print(arr)
    break
  k = k+1

print(arr.remove(arr[2]))