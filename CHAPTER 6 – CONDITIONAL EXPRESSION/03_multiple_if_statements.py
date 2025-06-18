age = int(input("Enter your age: "))

# If statement no. 1
if(age%2==0):
    print("age is even")
# End of if statement no. 1

# If statement no. 2
if(age>=18):
    print("you are above the age of consent") 
    print("Good for you")

elif(age<0):
    print("You are entering an invalid negative age")

else:
    print("you are below the age of consent")
# End of if statement no. 2

print("End of program")
