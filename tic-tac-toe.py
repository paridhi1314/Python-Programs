Python 3.9.5 (tags/v3.9.5:0a7dcbd, May  3 2021, 17:27:52) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> theBoard = {'top-L': ' ', 'top-M': ' ', 'top-R': ' ',
           'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ',
            'low-L': ' ', 'low-M': ' ', 'low-R': ' '}
>>> 
>>> theBoard
{'top-L': ' ', 'top-M': ' ', 'top-R': ' ', 'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ', 'low-L': ' ', 'low-M': ' ', 'low-R': ' '}
>>> import pprint
>>> pprint.pprint(theBoard)
{'low-L': ' ',
 'low-M': ' ',
 'low-R': ' ',
 'mid-L': ' ',
 'mid-M': ' ',
 'mid-R': ' ',
 'top-L': ' ',
 'top-M': ' ',
 'top-R': ' '}
>>> theBoard['mid-M'] = ''
>>> pprint.pprint(theBoard)
{'low-L': ' ',
 'low-M': ' ',
 'low-R': ' ',
 'mid-L': ' ',
 'mid-M': '',
 'mid-R': ' ',
 'top-L': ' ',
 'top-M': ' ',
 'top-R': ' '}
>>> theBoard['mid-M'] = 'X'
>>> pprint.pprint(theBoard)
{'low-L': ' ',
 'low-M': ' ',
 'low-R': ' ',
 'mid-L': ' ',
 'mid-M': 'X',
 'mid-R': ' ',
 'top-L': ' ',
 'top-M': ' ',
 'top-R': ' '}
>>> theBoard['mid-M'] = ' '
>>> pprint.pprint(theBoard)
{'low-L': ' ',
 'low-M': ' ',
 'low-R': ' ',
 'mid-L': ' ',
 'mid-M': ' ',
 'mid-R': ' ',
 'top-L': ' ',
 'top-M': ' ',
 'top-R': ' '}
>>> theBoard['mid-M'] = 'X'
>>> pprint.pprint(theBoard)
{'low-L': ' ',
 'low-M': ' ',
 'low-R': ' ',
 'mid-L': ' ',
 'mid-M': 'X',
 'mid-R': ' ',
 'top-L': ' ',
 'top-M': ' ',
 'top-R': ' '}
>>> theBoard['top-L'] = 'O'
>>> theBoard['top-M'] = 'O'
>>> theBoard['top-R'] = 'O'
>>>  pprint.pprint(theBoard)
 
SyntaxError: unexpected indent
>>> pprint.pprint(theBoard)
{'low-L': ' ',
 'low-M': ' ',
 'low-R': ' ',
 'mid-L': ' ',
 'mid-M': 'X',
 'mid-R': ' ',
 'top-L': 'O',
 'top-M': 'O',
 'top-R': 'O'}
>>> def printBoard(board):
	print(board['top-L'] + '|' + board['top-M'] + board['top-R'])
	print('-----')
	print(board['mid-L'] + '|' + board['mid-M'] + board['mid-R'])
	print('-----')
	print(board['low-L'] + '|' + board['low-M'] + board['low-R'])

	
>>> printBoard(theBoard)
O|OO
-----
 |X 
-----
 |  
>>> def printBoard(board):
	print(board['top-L'] + '|' + board['top-M'] + '|' + board['top-R'])
	print('-----')
	print(board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'])
	print('-----')
	print(board['low-L'] + '|' + board['low-M'] + '|' + board['low-R'])

	
>>> printBoard(theBoard)
O|O|O
-----
 |X| 
-----
 | | 
>>> type(42)
<class 'int'>
>>> 