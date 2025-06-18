# Python has an open() function for opening files. It takes 2 parameters: filename and mode
# open("filename", "mode of opening(read mode by default)")

f = open("file.txt","r") # r is for reading file you can also now write it cos it is default
data = f.read() # Read its contents
print(data) # Print its contents
f.close()
