# a = int(input("Enter marks "))
# b = int(input("Enter marks "))
# c = int(input("Enter marks "))

# if(a>=33 and b>=33 and c>=33 and (a+b+c)>=120):
#     print("congratulations you have passed in exam")
# else:
#     print("you have failed in exam, try again")

# OR

marks1 = int(input("Enter marks 1 "))
marks2 = int(input("Enter marks 2 "))
marks3 = int(input("Enter marks 3 "))

total_percentage = ((marks1 + marks2 + marks3)/300)*100

if(total_percentage>=40 and marks1>=33 and marks2>=33 and marks3>=33):
    print("You are passed:",total_percentage)
else:
    print("You failed, try again next year:",total_percentage)
