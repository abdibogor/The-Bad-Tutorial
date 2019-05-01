var=100
def sample():
    var=0
    print("Local value:", var)
    return
print("Global Value:", var)
sample()


"""
var=100
def sample(var):
    print("Local value:", var)
    return
print("Global Value:", var)
sample(var)
"""
