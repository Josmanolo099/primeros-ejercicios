#Diseñe una función hallar_mayor_menor(a,b) que tome como argumento dos números 
# y devuelva el mayor y menor de ellos.
def Mayor_menor (a,b) :
    if a>b:
        print("El numero mayor es "+a+" y el menor es "+b)
    else:
        print("El numero mayor es "+b+" y el menor es "+a)

print("determine que numero es mayor")
a=input("diguite un numero entero ")
b=input("diguite un numero entero ")
Mayor_menor (a,b)
