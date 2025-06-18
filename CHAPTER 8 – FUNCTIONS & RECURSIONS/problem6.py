def inch_to_cms(inch):
    cms = inch*2.54
    return cms

n = int(input("Enter value in inches: "))
print(f"The corresponding value in cms is {inch_to_cms(n)}")