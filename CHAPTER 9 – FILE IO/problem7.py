with open("log.txt") as f:
    lines = f.readlines()

lineno = 1
for i in lines:

    if("python" in i):
        print(f"Yes python is present. Line no. : {lineno} ")
        break
    lineno += 1
else:
    print("No python is not present")
