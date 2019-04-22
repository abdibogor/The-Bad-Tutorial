Python 3.4.0 (v3.4.0:04f714765c13, Mar 16 2014, 19:25:23) [MSC v.1600 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> address={}
>>> address["Abdibogoreh"]="abdirazak047@gmail.com"
>>> address["abdibogoreh"]="bogoreh_code@outlook.com"
>>> address["abdi"]="abdi_coding@outlook.fr"
>>> print(address)
{'abdi': 'abdi_coding@outlook.fr', 'Abdibogoreh': 'abdirazak047@gmail.com', 'abdibogoreh': 'bogoreh_code@outlook.com'}
>>> new={'apple':'fruit', 'iPhone':'Phone', 7:'a number'}
>>> new
{7: 'a number', 'apple': 'fruit', 'iPhone': 'Phone'}
>>> address.keys()
dict_keys(['abdi', 'Abdibogoreh', 'abdibogoreh'])
>>> address.values()
dict_values(['abdi_coding@outlook.fr', 'abdirazak047@gmail.com', 'bogoreh_code@outlook.com'])
>>> 
