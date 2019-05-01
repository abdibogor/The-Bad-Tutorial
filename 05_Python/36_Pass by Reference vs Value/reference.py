"""
employee={'Alex':1500,'John':1200,'Peter':1400}
def test(employee):
    new={'Buck':2000,'Stan':4000}
    employee.update(new)
    print("Inside the function", employee)
    return
test(employee)
print("Outside the function:", employee)
"""

employee={'Alex':1500,'John':1200,'Peter':1400}
def test(employee):
    employee={'Buck':2000,'Stan':4000}
    print("Inside the function", employee)
    return
test(employee)
print("Outside the function:", employee)
