Python 3.4.0 (v3.4.0:04f714765c13, Mar 16 2014, 19:25:23) [MSC v.1600 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> mylist=['one', 'two', 'three', 4, 5.0, 6+2j]
>>> mylist
['one', 'two', 'three', 4, 5.0, (6+2j)]
>>> print(mylist)
['one', 'two', 'three', 4, 5.0, (6+2j)]
>>> mylist[0]
'one'
>>> mylist[1:]
['two', 'three', 4, 5.0, (6+2j)]
>>> mylist * 3
['one', 'two', 'three', 4, 5.0, (6+2j), 'one', 'two', 'three', 4, 5.0, (6+2j), 'one', 'two', 'three', 4, 5.0, (6+2j)]
>>> newlist=[7, 'eight', 9.0]
>>> mylist + newlist
['one', 'two', 'three', 4, 5.0, (6+2j), 7, 'eight', 9.0]
>>> newlist[0]="seven"
>>> newlist
['seven', 'eight', 9.0]
>>> mytuple=('a word', 'a number', 10)
>>> mytuple
('a word', 'a number', 10)
>>> mytuple[0]
'a word'
>>> mytuple[1:]
('a number', 10)
>>> mytuple * 4
('a word', 'a number', 10, 'a word', 'a number', 10, 'a word', 'a number', 10, 'a word', 'a number', 10)
>>> mytuple[1]=55
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    mytuple[1]=55
TypeError: 'tuple' object does not support item assignment
>>> 
