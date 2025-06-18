s = {8, 7, 12, "Harry", [1,2]} # this will give error

# first we cant include list([1,2]) in set bucause list are mutable and not hashable
# tuple can be in a set because both are immutable and hashable
# second there is no indexing on set so we cant change(update) values in set
# but we can add and remove values in set

s = {8, 7, 12, "Harry", (1,2)} # this will not give error