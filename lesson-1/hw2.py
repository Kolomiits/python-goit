
a = input("Please Enter coefficient 'a': ")
a = int(a)
b = input("Please Enter coefficient 'b': ")
b = int(b)
c = input("Please Enter coefficient 'c': ")
c = int(c)
D = b * 2 - 4 * a * c
x1 = (-b + D * 0.5) / 2 * a
x2 = (-b - D * 0.5) / 2 * a

print(f"root of the equation x1 {x1}")
print(f"root of the equation x2 {x2}")