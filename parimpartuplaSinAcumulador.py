def parimpar(lista):
    if len(lista) == 0:
        return ([], [])
    else:
        #lLamada recursiva para ir obteniendo los valores de la lista
        impares, pares = parimpar(lista[1:])
        if lista[0] % 2 == 0:
            #insertamos en los pares si es par
            pares.insert(0,lista[0])
        else:
            #insertamos en los impares si es impar
            impares.insert(0,lista[0])
        return (impares, pares)

def casoDePrueba():
    try:
        longitud = int(input())
        if(longitud >= 0):
            numeros = input().split()
            lista = list(map(int, numeros))
            if(longitud == len(lista)):
                print(parimpar(lista))
            return True
    except:
        return False

if __name__ == "__main__":
    while casoDePrueba():
        pass
