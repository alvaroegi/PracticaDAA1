def hanoi(n,o,d,a):
    if n == 1:
        print("Mueve disco",n,"desde torre",o,"a torre",a)
        print("Mueve disco",n,"desde torre",a,"a torre",d)
    else:
        hanoi(n-1,o,d,a)
        print("Mueve disco",n,"desde torre",o,"a torre",a)
        hanoi(n-1,d,o,a)
        print("Mueve disco", n, "desde torre", a, "a torre", d)
        hanoi(n-1,o,d,a)

# Ejemplo de uso
def casoDePrueba():
    try:
        num = int(input())
        if(num > 0) and (num <= 9):
            hanoi(num,1,3,2)
            return True
    except:
        return False
if __name__ == "__main__":
    while casoDePrueba():
        pass

