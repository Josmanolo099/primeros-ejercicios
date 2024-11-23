#Definir una función inversa() que calcule la inversión de una cadena.
#  #Por ejemplo print palabra_inversa('universidad industrial de santander') 
# su programa entrega 'rednatnas ed lairtsudni dadisrevinu'
def Revers(palabra):
    for caracter in palabra:
        inversa=caracter+inversa
    return inversa
cadena=str(input("digite una palabra: \n"))
inversa=Revers(cadena)
print("la cade es",cadena," y su inversa es ",inversa)