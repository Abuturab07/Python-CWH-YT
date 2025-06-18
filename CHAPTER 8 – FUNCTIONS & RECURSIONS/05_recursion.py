# Recursion is a function which calls itself
# It is used to directly use a mathematical formula as function

def factorial(n):
    if(n==1 or n==0):
        return 1 # base condition which doesn’t call the function any further
    else:
        return n * factorial(n-1) # function calling itself
    
n = int(input("Enter a number: "))
print(f"Factorial of this number is {factorial(n)}")