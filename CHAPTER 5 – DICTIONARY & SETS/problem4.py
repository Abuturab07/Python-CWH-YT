s = set()
s.add(20)
s.add(20.0)
s.add('20') # length of s after these operations?

# in python 1 == 1.0 # output True, and set only takes unique values
# python doesnt check data type it only checks if numerically value is equal or not
print(s)
print(len(s))