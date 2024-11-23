#Diseñe un programa que permita establecer la relación entre dos números ingresados 
# y se cumplan las siguientes relaciones relación(a,b). Si el primer número es mayor
#  que el segundo, debe devolver "True". Si el primer número es menor que el segundo, 
# debe devolver "False" y Si ambos números son iguales, debe devolver un "Empate".
def Rel_num (c,d):
    if c>d:
        print("true")
    elif c<d:
         print("false")
    elif c==d:
         print("empate")

a=int(input("ingrese un numero entero: "))
b=int(input("ingrese un numero entero: "))
Rel_num (a,b)