l=[]
try:
    d=10/0

except ZeroDivisionError as e:
    print("you cannnot divide a no by 0 {0}".format (e ))
print("proceed")
input("hold")
try:
    print(l[0])
except IndexError as e:
    print("Not assigned any value to this index{0}".format(e))
try:
    l=[]
    print(l.get())
except AttributeError as e:
    print("list doesnot has get attribute".format(e))





