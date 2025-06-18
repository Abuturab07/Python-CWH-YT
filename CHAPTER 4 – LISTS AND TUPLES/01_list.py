# if we want to store muliple things of same or differnt type then we use list (also called array in other languages)
# Python lists are containers to store a set of values of any data type
# list are not immutable( you can change them)
# A list can be indexed just like a string

friends = ["apple","orange",5,345.06,False,"Aakash","Rohan"]
print(friends[0])
friends[0] = "grapes" # Unlike strings, list are mutable( you can change them)
print(friends[0])\

# list slicing
print(friends[0:2])
