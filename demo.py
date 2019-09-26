'''a="shreya"
print(type(a))

#for-loop
for i in range(10):
	print(range(5))
	print(i)
	print(list(range(5)))

#if-else
fi=int(input("Enter a no. below:\n"))
if fi>5:
	print("it is greater than 5")
else:
	print("it is less than 5")

#list
l=[3,"shreya",5,56.0,"rahul",7,23.8,"tushi"]
print(l[2])
print(l[2:6])
print(l[3:])
print(l[:5])
print(l*3)
l.append("last")
print(l)
l.pop()
print(l)
l.delete(3)
print(l)s
'''

#tuples
tuple1=('abcd',76,2.23,44,67)
tinytuple = (123, 'john')
print (tuple1)       
	# Prints complete tuple 
print (tuple1[0])       
	# Prints first element of the tuple 
print (tuple1[1:3])   
	# Prints elements starting from 2nd till 3rd  
print (tuple1[2:])   
	# Prints elements starting from 3rd element 
print (tinytuple * 2) 
	# Prints tuple two times
print (tuple1 + tinytuple) 
	# Prints concatenated tuple  
print (tuple1[:4])

