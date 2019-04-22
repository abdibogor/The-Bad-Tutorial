Python 3.4.0 (v3.4.0:04f714765c13, Mar 16 2014, 19:25:23) [MSC v.1600 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> print('Hello World!')
Hello World!
>>> str1="My string"
>>> str1
'My string'
>>> print (str1)
My string
>>> str2 = "My
SyntaxError: EOL while scanning string literal
>>> str2="""My
String"""
>>> str2
'My\nString'
>>> print (str2)
My
String
>>> print ('Hello World!')
Hello World!
>>> print ('What\'s up?')
What's up?
>>> print ('Hello World!'); print('What\'s up?')
Hello World!
What's up?
>>> str3="This is a string"
>>> str3
'This is a string'
>>> ================================ RESTART ================================
>>> str3
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    str3
NameError: name 'str3' is not defined
>>> 
