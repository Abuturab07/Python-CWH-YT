f = open("poems.txt")
content = f.read()

if("Twinke" in content):
    print("The word Twinke is present in the content")
else:
    print("The word Twinke is not presnt in the content")

f.close()

