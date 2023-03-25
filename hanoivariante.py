def hanoi(n,o,d,a):
    if n == 1:
        print("Mueve disco",n,"desde torre",o,"a torre",a)
        print("Mueve disco",n,"desde torre",a,"a torre",d)
    else:
        hanoi(n-1,o,a,d)
        print("Mueve disco",n,"desde torre",o,"a torre",a)
        hanoi(n-1, )
        print("Mueve disco", n, "desde torre", a, "a torre", d)
        hanoi(n-1,d,a,o)

# Ejemplo de uso
hanoi(2,1,2,3)




