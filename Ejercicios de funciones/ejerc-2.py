#Diseñe una función llamada area_perimetro_circulo(radio) que devuelva el perimetro y área de un círculo a partir de un radio.
import math 
def Area_perimetro_rec (r):
    area= math.pi*(pow(r,2))
    perimetro=2*math.pi*r
    return area, perimetro

print("Area y perimetro de un circulo")
c=float(input("digite el radio de un circulo"))
area,perimetro= Area_perimetro_rec (c)
print("El area del circulo es: ", round(area,3)," y el perimetro es: ",  round (perimetro,3))
