myobj=open("test.txt","w")
myobj.write("""This is so cool! Now I can create text files using python!""")
myobj.close()

myobj=open("test.txt","w")
myobj.write("""Let's see where this text goes!""")
myobj.close()


myobj=open("test.txt","r")
text=myobj.read()
print(text)
myobj.close()
