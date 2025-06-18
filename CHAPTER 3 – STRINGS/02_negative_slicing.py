name = "harry"

print(name[-4:-1])
print(name[1:4]) # covert negaive indexes to corresponding  positive indeces(index)

print(name[:3]) # is same as name[0:3]
print(name[:])  # is same as name[0:5]
print(name[1:]) # is same as name[1:5]
print(name[1:5])
Word = "amazing"
Word[:7] # word [0:7] – 'amazing'
Word[0:] # word [0:7] – 'amazing


# SLICING WITH SKIP VALUE
word = "amazing"
word[1: 6: 2]   # output= "mzn", here 2 skips 2 iteratons of word[1:6]