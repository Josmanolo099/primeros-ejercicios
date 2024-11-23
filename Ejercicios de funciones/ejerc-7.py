#Diseñe un algoritmo que realice el proceso de ordenar una lista dada con números enteros 
# y estos se repartan en dos listas pares e impares respectivamente. 
# Cree una función Separar(lista). Utilice los comandos nombrelista.sort() 
# para ordenar la lista y nombrelista.append()
def Separar(numeros):
    numeros.sort()
    # Creamos dos listas vacías para almacenar los números pares e impares
    lista_pares = []
    lista_impares = []
    # Recorremos la lista original
    for num in numeros:
        if num % 2 == 0:
            # Si el número es par, lo agregamos a la lista de pares
            lista_pares.append(num)
        else:
            # Si el número es impar, lo agregamos a la lista de impares
            lista_impares.append(num)

    # Devolvemos las dos listas resultantes
    return lista_pares, lista_impares
    
    
c=int(input("Digite la cantidad de numeros que quiere ingresar a la lista "))
lista=[]
i=int (1)
for i in range (c):
    a=input(" ingrese un numero")
    lista.append (a)
    i+=1
lista.sort()
pares, impares = Separar(lista)

print("Números pares:", pares)
print("Números impares:", impares)



