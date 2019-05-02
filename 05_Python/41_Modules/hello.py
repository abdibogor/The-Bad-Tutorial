Python 3.4.0 (v3.4.0:04f714765c13, Mar 16 2014, 19:25:23) [MSC v.1600 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> import sys
>>> sys.path
['', 'C:\\Python34\\Lib\\idlelib', 'C:\\Windows\\SYSTEM32\\python34.zip', 'C:\\Python34\\DLLs', 'C:\\Python34\\lib', 'C:\\Python34', 'C:\\Python34\\lib\\site-packages']
>>> import mymodule
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    import mymodule
ImportError: No module named 'mymodule'
>>> import mymodule
>>> mymodule.hello()
What's your name?
Abdoulrazak 
Hello Abdoulrazak  , have a nice day!
>>> mymodule.hello()
What's your name?
Abdibogoreh
Hello Abdibogoreh , have a nice day!
>>> 
