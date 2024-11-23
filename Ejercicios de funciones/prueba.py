def Separar(lista):
    # Primero, ordenamos la lista original
    lista.sort()

    # Creamos dos listas vacías para almacenar los números pares e impares
    lista_pares = []
    lista_impares = []

    # Recorremos la lista original
    for num in lista:
        if num % 2 == 0:
            # Si el número es par, lo agregamos a la lista de pares
            lista_pares.append(num)
        else:
            # Si el número es impar, lo agregamos a la lista de impares
            lista_impares.append(num)

    # Devolvemos las dos listas resultantes
    return lista_pares, lista_impares

# Ejemplo de uso:
c=int(input("Digite la cantidad de numeros que quiere ingresar a la lista "))
mi_lista = []
for i in range (c):
    a=int(input(" ingrese un numero: "))
    mi_lista.append (a)
    i+=1
pares, impares = Separar(mi_lista)

print("Números pares:", pares)
print("Números impares:", impares)
