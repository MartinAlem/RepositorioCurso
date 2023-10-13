def promedio(lista_numeros):
    
    suma_lista = sum(lista_numeros)
    print(f'la suma de todos los números de la lista es igual a: {suma_lista}')
    
    cant_num_lista = len(lista_numeros)
    print(f'la cantidad de números de la lista es igual a: {cant_num_lista}')

    promedio = suma_lista / cant_num_lista

    return promedio

if __name__ == "__main__":

    lista_numeros = [1,3,8,9,10]
    resultado = promedio(lista_numeros)

    print(f'el promedio de esta lista de números {lista_numeros} es igual a: {resultado}')


