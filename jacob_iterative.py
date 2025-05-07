a11 = int(input("Enter the value of a11 = "))
a12 = int(input("Enter the value of a12 = "))
a13 = int(input("Enter the value of a13 = "))

a21 = int(input("Enter the value of a21 = "))
a22 = int(input("Enter the value of a22 = "))
a23 = int(input("Enter the value of a23 = "))

a31 = int(input("Enter the value of a31 = "))
a32 = int(input("Enter the value of a32 = "))
a33 = int(input("Enter the value of a33 = "))

b1 = int(input("Enter the value of b1 = "))
b2 = int(input("Enter the value of b2 = "))
b3 = int(input("Enter the value of b3 = "))

x1 = x2 =x3 =0
e = float(input("Enter the value of error e= "))
condition = True

while condition:
    x = (b1-a12 * x2 - a13 *x3)/a11
    y = (b2 - a21 *x1 - a23 *x3)/a22
    z = (b3 - a31 *x1 - a32 * x2)/a33

    x = round(x,5)
    y = round(y,5)
    z = round(z,5)

    print("x = ",x, "y = ",y,"z =",z)
    
    e1 = abs(x1-x)
    e2 = abs(x2-y)
    e3 = abs(x3-z)

    x1=x
    x2=y
    x3=z
    
    condition = e1 > e and e2> e and e3> e

x = round(x,3)
y = round(y,3)
z = round(z,3)

print("x = ",x, "y = ",y,"z =",z)