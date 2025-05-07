def f(x):
    y = x*x*x + 2*x*x + 10*x - 20
    return y

def bisection(a,b):
    if (f(a)*f(b) >= 0):
        print("Incorrect Interval")
        return 
    c = a
    while (b-a) >= 0.0001:
        m = (a+b)/2
        if (f(m) == 0):
            break
        if(f(a)*f(m) < 0):
            b = m
        else:
            a=m
    print("The value of roois : ","%.4f" %m)

a = int(input("Enter the value of 'a': "))
b = int(input("Enter the value of 'b': "))
bisection(a,b)