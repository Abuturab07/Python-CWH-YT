class Demo:
    a = 4

object = Demo()
print(object.a) # Prints the class attribute because object(Instance) attribute is not present

object.a = 0 # Instance attrubute is set
print(object.a) # Prints the Instance attribute because object(Instance) attribute present

print(Demo.a) # Prints the class attribute, so the answer is no