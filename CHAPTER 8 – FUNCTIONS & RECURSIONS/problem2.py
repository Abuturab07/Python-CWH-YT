def f_to_c(f):
    c = 5*(f-32)/9
    return c

f = int(input("Inter temperature in F: "))
d = f_to_c(f)
print(f"{round(d,2)}°C")
