Python 3.9.5 (tags/v3.9.5:0a7dcbd, May  3 2021, 17:27:52) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> spam = 'Hello world!'
>>> spam.islower()
False
>>> spam = 'hello world'
>>> spam.islower()
True
>>> spam = 'HELLO WORLF'
>>> spam.isupper()
True
>>> spam = ''
>>> spam.isupper()
False
>>> spam.islower()
False
>>> 'Hello'.upper()
'HELLO'
>>> 'Hello'.upper().isupper()
True
>>> 'hello'isaplha()
SyntaxError: invalid syntax
>>> 'hello'.isalpha()
True
>>> 'hello123'.isalpha()
False
>>> 'hello123'.isalnum()
True
>>> '123'.isdecimsl()
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    '123'.isdecimsl()
AttributeError: 'str' object has no attribute 'isdecimsl'
>>> '123'.isdecimal()
True
>>> '     '.isspace()
True
>>> 'hello   ds'.isspace()
False
>>> 'This is Title '.istitle()
False
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
>>> 'Hello World'.startswith('Hello')
True
>>> 'Hello worl'.startswith('h')
False
>>> 'Helo world!'.endswith('!')
True
>>> 
>>> 
>>> 
>>> ','.join(['cats','rats','bats'])
'cats,rats,bats'
>>> 
>>> 
>>> 
>>> 'My name is Paridhi'.split()
['My', 'name', 'is', 'Paridhi']
>>> 'My name is Paridhi'.split('a')
['My n', 'me is P', 'ridhi']
>>> 'Hello'.rjust(10)
'     Hello'
>>> 'Hello'.rjust(20,'*')
'***************Hello'
>>> 'Hello'.ljust(25,'-')
'Hello--------------------'
>>> 'Hello'.center(20,'=')
'=======Hello========'
>>> 
>>> 
>>> 
>>> 'Hello'.rjust(10)
'     Hello'
>>> spam = 'Hello'.rjust(10)
>>> spam.strip()
'Hello'
>>> 
>>> 
>>> 
>>> spam = spam.strip()
>>> spam
'Hello'
>>> '      x  '.strip()
'x'
>>> 
>>> 
>>> 
>>> spam = 'Hello There'
>>> spam.replace('e','XYZ')
'HXYZllo ThXYZrXYZ'
>>> 
>>> import pyperclip
>>> pyperclip.copy('Helo!!!!!!')
>>> pyperclip.paste()
'Helo!!!!!!'
>>> 