'''l= [3, 1, 8, 6, 5]
print("before sorting list is{0}".format(l))
l.sort()
print("after sorting list is{0}".format(l))



def getValues(a, pi=3.14, c=None):
    #print(pi)
    input("hold")
    if c is not None:
        print(c)
        return a + pi + c
    return a + pi

def getSum(a,b):
    return a+b

def getdiffrence(a,b):
    if isinstance(a,(int,float)):
        return  a-b
    else:
        print ("Pass either integer int or float")

print("Hi")
if __name__ == '__main__':
    a = 2.5
    b = 8.6
    c=2
    d=2
    print((c == d))
    print((c is d))

    # print(getdiffrence(a,b))
   # print(getSum(a,b))
    print(getValues(1, 2, 5))
    '''


