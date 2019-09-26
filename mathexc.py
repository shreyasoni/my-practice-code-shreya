import math
def sqrt(x):
    if not isinstance(x,(int,float)):
        raise TypeError('x must be integer')
    elif x < 0:
        raise ValueError('x cannot be negative')
    else:
        return math.sqrt(x)
try:
    print(sqrt("9"))
    print(sqrt(12))
except Exception as e:
    print(e.__class__)
    #print("error {0}".format(e) )