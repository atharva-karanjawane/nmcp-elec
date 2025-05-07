n = int(input("Enter no. of data points n "))
print("Enter x values ", end=" ")

x = []

for i in range(0,n):
    z = input( 'x' + str(i) + "=")
    x.append(float(z))

print(x)

print("Enter y values", end=" ")
y = []
for j in range(0,n):
    m = input('y' + str(i) + "=")
    y.append(float(m))

print(y)

xr = int(input("Enter value of xr: "))
sum = 0

for i in range(0,n):
    prod = 1
    for j in range(0,n):
        if i!=j:
            prod = prod*( (xr-x[j]/ x[i]-x[j] ))

    sum = sum + prod + y[i]
print("f(x) = ",sum)
