# unlike list tuple is immutable data type like strings
a = (1,2,3,4) # this is a tuple
print(type(a))
b = () # empty tuple
c = (1) # this is int
d = (1,) # this is single elemnt tuple
print(type(b),type(c),type(d))


x = (1,45,342,3424,False,"Rohan","Shivam")
# x[0] = 453 # this will give error because you cant change tuple
print(x)