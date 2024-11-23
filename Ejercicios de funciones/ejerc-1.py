# Diseñe una función llamada area_perimtero_rectangulo(base, altura) que devuelva 
# el perimetro y área del rectangulo a partir de una base y una altura.
def Area_perimetro_rec (b,h):
    area=int(b*h)
    perimetro=int(2*b+2*h)
    return area, perimetro

print("Area y perimetro de un rectangulo")
c=int(input("digite la base del rectangulo"))
a=int(input("digite la altura del rectangulo"))
area=int
perimetro=int
area,perimetro= Area_perimetro_rec (c,a)
print("El area del rectangulo es: ",area," y el perimetro es: ",perimetro)
