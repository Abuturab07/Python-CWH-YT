a = int(input("Enter number a: "))
b = int(input("Enter number b: "))
c = int(input("Enter number c: "))
d = int(input("Enter number d: "))

if(a>b and a>c and a>d):
    print("a is greatest",a)
elif(b>a and b>c and b>d):
    print("b is greatest",b)
elif(c>a and c>b and c>d):
    print("c is greatest",c)
elif(d>a and d>b and d>c):
    print("d is greatest",d)