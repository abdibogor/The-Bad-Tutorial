"""
print("Enter numerator:")
num=input()
print("Enter denominator:")
den=input()
res=int(num)/int(den)
print(res)
"""
print("Enter numerator:")
num=input()
print("Enter denominator:")
den=input()
try:
      res=int(num)/int(den)
    except:
            print("You can't divide by zero baby!")
    else:
print("Result:", res)
