def insertSort(n,l):
    lon = len(l)
    if (lon == 0):
        #si la lista es vacía nos devuelve solo la lista con el elemento a insertar
        return [n]
    elif(n > l[lon-1]):
        #si el número es mayor que el último elemento de la lista lo concatenamos al final
        return l + [n]
    else:
        #si no lo es, seguimos realizando llamadas recursivas (sin perder sus valores, por eso vamos concatenando al final los valores ya calculados
        return insertSort(n,l[:-1]) + [l[lon-1]]

def casoDePrueba():
    try:
        longitud = int(input())
        if(longitud >= 0):
            numeros = input().split()
            num = int(input())
            lista = list(map(int, numeros))
            if(longitud == len(lista)):
                sol = insertSort(num,lista)

            for i in range(len(sol)-1):
                print(sol[i], end=" ")
            print(sol[len(sol)-1])

            return True
    except:
        return False

if __name__ == "__main__":
    while casoDePrueba():
        pass