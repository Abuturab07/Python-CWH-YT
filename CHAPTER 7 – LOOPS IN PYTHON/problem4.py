n = int(input("enter your number: "))

for i in range(2,n):
    if((n%i)==0):
        print("not prime")
        break
else:
    print("prime")