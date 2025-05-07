n = int(input("Enter number of data points n: "))
print("Enter x values: ",end=" ")
x = []

for i in range(0,n):
    z = input('x' + str(i) + '=')
    x.append(float(z))
print(x)

print("Enter y values: ",end=" ")
y = []

for j in range(0,n):
    m = input('y' + str(j) + '=')
    y.append(float(z))
print(y)

xx = []
for w in range(0,n):
    (xx.append(x[w]*x[w]))
print(" xx: ",xx)

xy = []
for t in range(0,n):
    (xy.append(x[t]*y[t]))
print(" xy: ",xy)
sumx = sumy = sumx2 = sumxy = 0

for i in range(0,n):
    sumx = sumx + x[i]
    sumy = sumy + y[i]
    sumx2 = sumx2 + xx[i]
    sumxy = sumxy + xy[i]

print("Sum x: ",sumx)
print("Sum y: ",sumy)
print("Sum xx: ",sumx2)
print("Sum xy: ",sumxy)

Dx = (sumy*sumx) - (sumxy*n)
Dy = (sumx*sumxy) - (sumx2*sumy)
D = (sumx*sumx) - (sumx2*n)

a = round((Dx/D),4)
b = round((Dy/D),4)
print("Value of a: ",a)
print("Value of b: ",b)

print("The Straight line using LSM: "," y = ",a, " + ",b,"x")
