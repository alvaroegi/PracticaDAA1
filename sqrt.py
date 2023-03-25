import sys

def NewtonRaphson(f,n,epsilon,a):
    if(f(n,a) == 0) or (abs(f(n,a)) < epsilon):
        return n
    else:
        aux = n - f(n,a) / df(n)
        return NewtonRaphson(f,aux,epsilon,a)

def f(x,a):
    return x*x - a

def df(x):
    return 2*x

def casoDePrueba():
    try:
        num = float(input())
        if(num >= 0):
            sol = NewtonRaphson(f, num, pow(10, -6), num)
            #truncar = math.trunc(NewtonRaphson(f, num, pow(10, -6), num) * 10 ** 4) / 10 ** 4
            #print("{:.4f}".format(truncar))
            print(format(sol,'.4f'))
            #print(sol)
            return True
    except:
        return False
if __name__ == "__main__":
    while casoDePrueba():
        pass

