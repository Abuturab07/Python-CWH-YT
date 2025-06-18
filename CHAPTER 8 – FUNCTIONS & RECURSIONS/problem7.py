l = ["harry", "rohan", "shubham", "an"]

def remove(l, word):
    n = []
    for item in l:  
        if not(item == word):
            n.append(item.strip(word))
    return n

print(remove(l, "an"))