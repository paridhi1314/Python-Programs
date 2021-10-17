dic = {10:'A',20:'B',30:'C',40:'D'}
dic1 = {70:'X',80:'Y'}

dic2={}
for i in (dic,dic1):
    dic2.update(i)
print(dic2)