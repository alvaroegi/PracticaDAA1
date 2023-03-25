def parimpar(lista,sol):
    lon = len(lista)
    if(lon == 0):
        return sol
    else:
        if(lista[0] % 2 == 0):
            sol[1].append(lista[0])
        else:
            sol[0].append(lista[0])

        return parimpar(lista[1:],sol)


def casoDePrueba():
    try:
        longitud = int(input())
        if(longitud >= 0):
            numeros = input().split()
            lista = list(map(int, numeros))
            if(longitud == len(lista)):
                print(parimpar(lista,([],[])))
            return True
    except:
        return False

if __name__ == "__main__":
    while casoDePrueba():
        pass
