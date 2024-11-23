##class UISBarbosa():
##    def __init__(self) -> None:
##        self.nombre=input("digite su nombre: ")
##        self.apellido=input("digite su apellido: ")
##        self.dc=input("digite el documento de identidad: ")
##        self.fcn=input("digite su fecha de nacimiento: ")
##        self.ht=float(input("digite las horas trabajadas: "))
##
##    def imprimir(self):
##        print(f"nombre: {self.nombre}, Apellido: {self.apellido}, Documento: {self.dc}, fecha de nacimiento: {self.fcn}, Horas trabajada:  {self.ht}")
##class Vigilancia(UISBarbosa):
##    def __init__(self) -> None:
##        super(). __init__()
##        self.turno=input("digite el turno dia o noche : ")
##        self.lugar=input("digite el lugar donde tiene el turno: ")
##        self.sueldo()
##    def sueldo(self):
##        if self.turno.lower() == "dia":
##            self.precio=self.ht*9500
##            print('El salario es: ',self.precio)
##            self.imprimir()
##        else: 
##            self.precio=self.ht*16000
##            print('El salario es: ',self.precio)
##    def imprimir(self):
##        print(f"nombre:{self.nombre}, Apellido: {self.apellido}, Documento:{self.dc}, fecha de nacimiento:{self.fcn}, Horas trabajada: {self.ht}, Sueldo: {self.precio}")
##
##class Adminitrativo(UISBarbosa):
##    def __init__(self) -> None:
##        super(). __init__()
##        self. sueldo()
##    def sueldo(self):
##        self.precio=self.ht*11000
##        print('El salario es: ',self.precio)
##        self.funciones()
##    def funciones(self):
##        self.dependencia=input("diga a que dependencia pertenece:")
##        self.funcion=input("ingrese que funcion cumple:\n")
##        self.imprimir()
##    def imprimir(self):
##        print(f"nombre:{self.nombre}, Apellido: {self.apellido}, Documento:{self.dc}, fecha de nacimiento:{self.fcn}, Horas trabajada: {self.ht},Dependencia: {self.dependencia}, Sueldo: {self.precio}")
##        print("funcion:")
##        print(self.funcion)
##class Auxiliares(Adminitrativo):
##    def __init__(self) -> None:
##        super(). __init__()
##        
##    def funciones(self):
##        self.funcion=input("ingrese que funcion cumple:\n")
##        self.imprimir()
##    def imprimir(self):
##        print(f"nombre:{self.nombre}, Apellido: {self.apellido}, Documento:{self.dc}, fecha de nacimiento:{self.fcn}, Horas trabajada: {self.ht},Sueldo: {self.precio}")
##        print("funcion:")
##        print(self.funcion)
##def Menu():
##    while True:
##            print("""\nUis sede Barbosa""")
##            print("""***************************************************""")
##            op=input("elija una opcion\n1. vigilante\n2. Administrativo\n3. Auxiliares\n4. salir\n ")
##            if op== '1':
##                Vigilancia()
##            elif op=='2':
##                Adminitrativo()
##            elif op == '3':
##                Auxiliares()
##            elif op == 4:
##                break
##            else :
##                print("opcion incorrecta")
##Menu()


# from datetime import datetime

# class UISBarbosa:
#     def __init__(self) -> None:
#         self.nombre = input("Digite su nombre: ")
#         self.apellido = input("Digite su apellido: ")
#         self.dc = input("Digite el documento de identidad: ")
#         self.fcn = input("Digite su fecha de nacimiento (dd/mm/yyyy): ")
#         self.ht = float(input("Digite las horas trabajadas: "))

#     def imprimir(self):
#         print(f"Nombre: {self.nombre}, Apellido: {self.apellido}, Documento: {self.dc}, Fecha de nacimiento: {self.fcn}, Horas trabajadas: {self.ht}")

# class Vigilancia(UISBarbosa):
#     def __init__(self) -> None:
#         super().__init__()
#         self.turno = input("Digite el turno (día o noche): ").strip().lower()
#         self.lugar = input("Digite el lugar donde tiene el turno: ")
#         self.sueldo()

#     def sueldo(self):
#         tarifa = 9500 if self.turno == "dia" else 16000
#         self.precio = self.ht * tarifa
#         print('El salario es:', self.precio)
#         self.imprimir()

#     def imprimir(self):
#         super().imprimir()
#         print(f"Sueldo: {self.precio}, Turno: {self.turno.capitalize()}, Lugar: {self.lugar}")

# class Administrativo(UISBarbosa):
#     def __init__(self) -> None:
#         super().__init__()
#         self.sueldo()

#     def sueldo(self):
#         self.precio = self.ht * 11000
#         print('El salario es:', self.precio)
#         self.funciones()

#     def funciones(self):
#         self.dependencia = input("Diga a qué dependencia pertenece: ")
#         self.funcion = input("Ingrese la función que cumple: ")
#         self.imprimir()

#     def imprimir(self):
#         super().imprimir()
#         print(f"Dependencia: {self.dependencia}, Sueldo: {self.precio}")
#         print(f"Función: {self.funcion}")

# class Auxiliares(Administrativo):
#     def funciones(self):
#         self.funcion = input("Ingrese la función que cumple: ")
#         self.imprimir()

#     def imprimir(self):
#         super().imprimir()
#         print(f"Función: {self.funcion}")

# def menu():
#     while True:
#         print("""\nUis Sede Barbosa
# ***************************************************
# 1. Vigilante
# 2. Administrativo
# 3. Auxiliares
# 4. Salir
# ***************************************************""")
#         op = input("Elija una opción: ")
#         if op == '1':
#             Vigilancia()
#         elif op == '2':
#             Administrativo()
#         elif op == '3':
#             Auxiliares()
#         elif op == '4':
#             print("Saliendo del sistema...")
#             break
#         else:
#             print("Opción incorrecta, por favor intente de nuevo.")

# menu()
import pandas as pd
import os
from datetime import datetime, date, timedelta

class Tienda:
    def __init__(self) -> None:
        self.productos1_file = 'productos_electronicos.csv'
        self.productos2_file = 'productos_alimenticios.csv'
        self.ventas_file = 'ventas.csv'
        self.Menu()
    
    def Agregar(self):
        while True:
            op = input("Marque: \n1. Para agregar un producto electrónico\n2. Para agregar un producto alimenticio\n3. Para salir\n")
            if op == '1':
                electronico = Electronico()
                electronico.Guardar(self.productos1_file)
            elif op == '2':
                alimento = Alimentos()
                alimento.Guardar(self.productos2_file)
            elif op == '3':
                print("Saliendo al menú principal...")
                return
            else:
                print("Número errado, intente nuevamente.")
            
    def Vender(self):
        print("Funcionalidad de ventas no implementada todavía.")
    
    def Mostrar(self):
        while True:
            op = input("Marque: \n1. Para ver los productos electrónicos\n2. Para ver los productos alimenticios\n3. Para salir\n")
            if op == '1':
                self.mostrar_productos(self.productos1_file)
            elif op == '2':
                self.mostrar_productos(self.productos2_file)
            elif op == '3':
                print("Saliendo al menú principal...")
                return
            else:
                print("Número errado, intente nuevamente.")
    
    def mostrar_productos(self, archivo):
        if os.path.exists(archivo):
            producto = pd.read_csv(archivo)
            print("Listado de productos:")
            print(producto)
        else:
            print("No hay registros de productos.")
    
    def Menu(self):
        while True:
            opcion = input("Elija: \n1. Agregar producto \n2. Mostrar productos \n3. Vender \n4. Salir\n")
            if opcion == '1':
                self.Agregar()
            elif opcion == '2':
                self.Mostrar()
            elif opcion == '3':
                self.Vender()
            elif opcion == '4':
                print("Saliendo del programa...")
                break
            else:
                print("Opción incorrecta, intente nuevamente.")

class Electronico:
    def __init__(self) -> None:
        self.nombre = input("Ingrese el nombre del producto electrónico: ")
        self.precio = float(input("Ingrese el precio del producto: "))
        self.cantidad = int(input("Ingrese la cantidad del producto: "))
        self.garantia = f"La garantía es de un año y comienza a partir de: {date.today()}"
    
    def Guardar(self, archivo):
        producto_nuevo = pd.DataFrame({
            'nombre': [self.nombre],
            'precio': [self.precio],
            'cantidad': [self.cantidad],
            'garantia': [self.garantia]
        })
        if os.path.exists(archivo):
            productos_existentes = pd.read_csv(archivo)
            productos_actualizados = pd.concat([productos_existentes, producto_nuevo], ignore_index=True)
            productos_actualizados.to_csv(archivo, index=False)
        else:
            producto_nuevo.to_csv(archivo, index=False)
        print("Producto electrónico guardado con éxito.")

class Alimentos:
    def __init__(self) -> None:
        self.nombre = input("Ingrese el nombre del producto alimenticio: ")
        self.precio = float(input("Ingrese el precio del producto: "))
        self.cantidad = int(input("Ingrese la cantidad del producto: "))
        self.vencimiento = date.today() + timedelta(days=60)
    
    def Guardar(self, archivo):
        producto_nuevo = pd.DataFrame({
            'nombre': [self.nombre],
            'precio': [self.precio],
            'cantidad': [self.cantidad],
            'vencimiento': [self.vencimiento]
        })
        if os.path.exists(archivo):
            productos_existentes = pd.read_csv(archivo)
            productos_actualizados = pd.concat([productos_existentes, producto_nuevo], ignore_index=True)
            productos_actualizados.to_csv(archivo, index=False)
        else:
            producto_nuevo.to_csv(archivo, index=False)
        print("Producto alimenticio guardado con éxito.")

# Instanciar la clase principal para ejecutar el programa
if __name__ == "__main__":
    Tienda()

