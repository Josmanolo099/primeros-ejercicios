#Escribir un programa que le diga al usuario que ingrese una cadena. 
# El programa tiene que evaluar la cadena y decir cuántas letras mayúsculas tiene
a="si"
while a=="si":
    cont=0
    cont1=0
    cadena=input("ingrese una cadena de texto: \n")
    for i in cadena :
        if i.isupper()==True:
            cont+=1
        else:
            cont1+=1
    print("la cantidad de letras mayusculas de la cadena es",cont)
    print("la cantidad de letras minuscula de la cadena es",cont1)
    a=(input("desea escribir otra cadena: ").lower())
