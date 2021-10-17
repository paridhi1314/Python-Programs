Python 3.9.5 (tags/v3.9.5:0a7dcbd, May  3 2021, 17:27:52) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> s1 = {1,2,3,4}
>>> s2 = {3,4,5,6}
>>> s1.union(s2)
{1, 2, 3, 4, 5, 6}
>>> s1 | s2
{1, 2, 3, 4, 5, 6}
>>> s1.intersection(s2)
{3, 4}
>>> s1 & s2
{3, 4}
>>> s1 and s2
{3, 4, 5, 6}
>>> s1.difference(s2)
{1, 2}
>>> s1-s2
{1, 2}
>>> s2-s1
{5, 6}
>>> s1.symmetric_difference(s2)
{1, 2, 5, 6}
>>> s1 ^ s2
{1, 2, 5, 6}
>>> print(s1)
{1, 2, 3, 4}
>>> print(s2)
{3, 4, 5, 6}
>>> s1.difference_update(s2)
>>> print(s1)
{1, 2}
>>> s1 = s1-s2
>>> s1
{1, 2}
>>> t1 = ()
>>> t2 = tuple()
>>> type(t1)
<class 'tuple'>
>>> type(t2)
<class 'tuple'>
>>> s1 = {}
>>> s2 = set()
>>> type(s1)
<class 'dict'>
>>> type(s2)
<class 'set'>
>>> 
>>> 


>>> 

>>> 


>>> 

>>> 


>>> 

>>> 


>>> 

>>> 

>>> 

>>> 


>>> 
>>> 
>>> t = (10,20,30,40)
>>> print(t)
(10, 20, 30, 40)
>>> t = (10,20,10,2.3,"abc")
>>> t
(10, 20, 10, 2.3, 'abc')
>>> t = (10,20,30,40,50)
>>> t[1]
20
>>> t[-2]
40
>>> t[:]
(10, 20, 30, 40, 50)
>>> t = (10,20,10,30,10)
>>> t.count(10)
3
>>> t.index(30)
3
>>> t = (10,20,30)
>>> t = (10,20,[30,40[)
	    
SyntaxError: closing parenthesis ')' does not match opening parenthesis '['
>>> 
>>> t = (10,20,[30,40])
>>> t
(10, 20, [30, 40])
>>> t[2]
[30, 40]
>>> t[2].append(50)
>>> t[2]
[30, 40, 50]
>>> t
(10, 20, [30, 40, 50])
>>> t[2].remove(30)
>>> t
(10, 20, [40, 50])
>>> d = {10:"A",20:"A",30:"A"}
>>> print(d)
{10: 'A', 20: 'A', 30: 'A'}
>>> d = {10:"A",10:"B",10:"C"}
>>> d
{10: 'C'}
>>> d = {10:"A",20:"B",30:"C"}
>>> d
{10: 'A', 20: 'B', 30: 'C'}
>>> d.pop()
Traceback (most recent call last):
  File "<pyshell#68>", line 1, in <module>
    d.pop()
TypeError: pop expected at least 1 argument, got 0
>>> d.popitem()
(30, 'C')
>>> d
{10: 'A', 20: 'B'}
>>> d.pop(10)
'A'
>>> d
{20: 'B'}
>>> d.update({50:'X'})
>>> d
{20: 'B', 50: 'X'}
>>> d = {10:20}
>>> d= {(10,20) : (30,40)}
>>> d = {10: [20,30]}
>>> d = {10:'A', 20:'B',30:'C',40:'d'}
>>> print(d)
{10: 'A', 20: 'B', 30: 'C', 40: 'd'}
>>> d.get(30)
'C'
>>> d.values()
dict_values(['A', 'B', 'C', 'd'])
>>> d.keys()
dict_keys([10, 20, 30, 40])
>>> d.clear