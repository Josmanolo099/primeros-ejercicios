#clase 24 de agosto

#a=input("ingrese su nombre\n")
#f=int(input("ingrese su año de nacimiento\n"))
#edad=2024-f
#if(edad>=18):
   # print(a," tiene ",edad," años")
#else:
    # print(a," usted es menor de edad ")

#a=float(input("digite el lado 1 del un triangulo: "))
#b=float(input("digite el lado 2 del un triangulo: "))
#c=float(input("digite el lado 3 del un triangulo: "))

#if(a+b>c and a+c>b and b+c>a):
##    print("los datos ingresados pertenecen a un  triangulo")
##    if(a==b==c):
##         print("el triangulo es equilatero")
##    elif(a!=b!=c):
##         print("el triangulo es escaleno")
##    else:
##         print("el triangulo es isosceles")
##else:
##    print("los datos ingresados no pertenecen a un  triangulo")

##import math
##op = (input("""Elija una figura:
##        1- cuadrado
##        2- Circunferencia
##        3- Triangulo
##        4- Rombo
##        5- Trapecio /n"""  
##    ))
##if op=='1':
##        print ("la figura seleccionada es un cuadrado ")
##        l1=float(input("ingrese el lado "))
##        p=float(l1*4)
##        a=l1*l1
##        print("el perimetro del cuadrado es ",p," el area del cuadrado es ",a)
##elif op=='2':
##    print ("la figura seleccionada es una circunferencia")
##    r=float(input("ingrese el radio "))
##    p=2*math.pi*r
##    a=math.pi*pow(r,2)
##    print("el perimetro de la circunferencia es ",p," el area de la circunferencia es ",a)
##elif op=='3':
##    print ("la figura seleccionada es un triangulo")
##    l1=float(input("digite el lado 1 del un triangulo: "))
##    l2=float(input("digite el lado 2 del un triangulo: "))
##    l3=float(input("digite el lado 3 del un triangulo: "))
##
##    if(l1+l2>l3 and l1+l3>l1 and l2+l3>l1):
##        print("los datos ingresados pertenecen a un  triangulo")
##        if(l1==l2==l3):
##            print("el triangulo es equilatero")
##            p=l1+l2+l3
##            s=(l1+l2+l3)/2
##            a=math.sqrt(s(s-l1)(s-l2)(s-l3))
##            print("el perimetro del triangulo  es ",p," el area del triangulo es ",a)
##        elif(l1!=l2!=l3):
##            print("el triangulo es escaleno")
##            p=l1+l2+l3
##            s=(l1+l2+l3)/2
##            a=math.sqrt(s(s-l1)(s-l2)(s-l3))
##            print("el perimetro del triangulo  es ",p," el area del triangulo es ",a)
##        else:
##            print("el triangulo es isosceles")
##            p=l1+l2+l3
##            s=(l1+l2+l3)/2
##            a=math.sqrt(s(s-l1)(s-l2)(s-l3))
##            print("el perimetro del triangulo  es ",p," el area del triangulo es ",a)
##   # else:
##    #print("los datos ingresados no pertenecen a un  triangulo")
##
##elif op=='4':
##    print ("la figura seleccionada es un Rombo")
##    l1=float(input("ingrese el lado"))
##    d=float(input("ingrese la diagonal mayor"))
##    d1=float(input("ingrese la diagonal menor"))
##    p=l1*4
##    a=(d*d1)/2
##    print("el perimetro del rombo  es ",p," el area del rombo es ",a)
##
##elif op=='5':
##    print ("la figura seleccionada es un trapecio")
##    h=float(input("ingrese la altura"))
##    b=float(input("ingrese la base mayor"))
##    c=float(input("ingrese la base menor"))
##    p=(c+b)*h
##    a=(c+b)*h/2
##    print("el perimetro del trapecio  es ",p," el area del trapecio es ",a)
##      
##else :
##    print(str("haz seleccionado una opcion erronea"))


##lista = ["bancolombia","davivienda","BBVA","banco de bogota"]
##a=input("ingrese el nombre del banco\n")
##if a in lista :
##    print("tenenemos convenio con este banco")
##else:
##    print("no tenenemos convenio con este banco")
##
##
##l=[0]
##entrada=int(input("ingrese un numero  "))
##l=0
##while entrada>=l[i] :
##    l.append(entrada)
##    i+=1
##    entrada=int(input("ingrese un numero  "))
##    while entrada<=l[i]:
##        print("ingrese numero  mayor al anterior")
##        entrada=int(input("ingrese un numero  "))

##while True :
##    import math
##    op = (input("""Elija una figura:
##            1- cuadrado
##            2- Circunferencia
##            3- Triangulo
##            4- Rombo
##            5- Trapecio /n"""  
##        ))
##    if op=='1':
##            print ("la figura seleccionada es un cuadrado ")
##            l1=float(input("ingrese el lado "))
##            p=float(l1*4)
##            a=l1*l1
##            print("el perimetro del cuadrado es ",p," el area del cuadrado es ",a)
##            break
##    elif op=='2':
##        print ("la figura seleccionada es una circunferencia")
##        r=float(input("ingrese el radio "))
##        p=2*math.pi*r
##        a=math.pi*pow(r,2)
##        print("el perimetro de la circunferencia es ",p," el area de la circunferencia es ",a)
##    elif op=='3':
##        print ("la figura seleccionada es un triangulo")
##        l1=float(input("digite el lado 1 del un triangulo: "))
##        l2=float(input("digite el lado 2 del un triangulo: "))
##        l3=float(input("digite el lado 3 del un triangulo: "))
##
##        if(l1+l2>l3 and l1+l3>l1 and l2+l3>l1):
##            print("los datos ingresados pertenecen a un  triangulo")
##            if(l1==l2==l3):
##                print("el triangulo es equilatero")
##                p=l1+l2+l3
##                s=float((l1+l2+l3)/2)
##                x1=(s-l1)
##                x2=(s-l2)
##                x3=(s-l3)
##                a=math.sqrt(s*x1*x2*x3)
##                print("el perimetro del triangulo  es ",p," el area del triangulo es ",a)
##            elif(l1!=l2!=l3):
##                print("el triangulo es escaleno")
##                p=l1+l2+l3
##                s=float((l1+l2+l3)/2)
##                x1=(s-l1)
##                x2=(s-l2)
##                x3=(s-l3)
##                a=math.sqrt(s*x1*x2*x3)
##                print("el perimetro del triangulo  es ",p," el area del triangulo es ",a)
##            else:
##                print("el triangulo es isosceles")
##                p=l1+l2+l3
##                s=float((l1+l2+l3)/2)
##                x1=(s-l1)
##                x2=(s-l2)
##                x3=(s-l3)
##                a=math.sqrt(s*x1*x2*x3)
##                print("el perimetro del triangulo  es ",p," el area del triangulo es ",a)
##    # else:
##        #print("los datos ingresados no pertenecen a un  triangulo")
##        break
##    elif op=='4':
##        print ("la figura seleccionada es un Rombo")
##        l1=float(input("ingrese el lado"))
##        d=float(input("ingrese la diagonal mayor"))
##        d1=float(input("ingrese la diagonal menor"))
##        p=l1*4
##        a=(d*d1)/2
##        print("el perimetro del rombo  es ",p," el area del rombo es ",a)
##        break
##    elif op=='5':
##        print ("la figura seleccionada es un trapecio")
##        h=float(input("ingrese la altura"))
##        b=float(input("ingrese la base mayor"))
##        c=float(input("ingrese la base menor"))
##        p=(c+b)*h
##        a=(c+b)*h/2
##        print("el perimetro del trapecio  es ",p," el area del trapecio es ",a)
##        break
##    else :
##        print(str("haz seleccionado una opcion erronea"))
##


# a=int(input("ingrese un numero "))
# for b in range (21):
#     c=a*b
#     print(c)

##----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# clase 31-08-2024 FUNCIONES
# def hoy ():
#     print("bienvenido a la clase")

# a=hoy()
# print(a)

# def Sumar(x1,x2):
#     resultado=x1+x2
#     print(resultado)

# a=float(input("ingrese un numero: "))
# b=float(input("ingrese un numero: "))
# sumar(a,b)

