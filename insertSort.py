def insertSort(n,l,p):
    lon = len(l)
    if(lon == 0):
        if(n < p[0]):
            p.insert(0,n)
        return p
    elif(n > l[lon-1]):
        p.insert(0,n)
        aux = l + p
        return aux
    else:
        p.insert(0,l[lon-1])
        return insertSort(n,l[:-1],p)

def casoDePrueba():
    try:
        longitud = int(input())
        if(longitud >= 0):
            numeros = input().split()
            num = int(input())
            lista = list(map(int, numeros))
            if(longitud == len(lista)):
                sol = insertSort(num,lista,[])

            for i in range(len(sol)-1):
                print(sol[i], end=" ")
            print(sol[len(sol)-1])

            return True
    except:
        return False

if __name__ == "__main__":
    while casoDePrueba():
        pass