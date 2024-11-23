# class Agenda:
#     def __init__(self) -> None:
#         self.contactos=[]
#         self.Menu()
#     def Lista(self):
#         if not self.contactos:
#             print("La agenda está vacía.")
#         else:
#             for i, contacto in enumerate(self.contactos, 1):
#                 print(f'{i}. {contacto}')
#     def Añadir(self):
#         self.nombre= input("Ingrese el nombre: ")
#         self.correo=input("ingrese el correo electronico: ")
#         self.numero=input("ingrese el numero de telefono: ")
#         self.contactos.append({'Nombre':self.nombre,'Correo ':self.correo,'Telefono ':self.numero})
#         print("contacto guardado")
#         self.Menu()
#     def Buscar(self):
#         encontrar = input("Digite el nombre de la persona que quiere buscar: ")
#         encontrado = False
#         for contacto in self.contactos:
#             if contacto['Nombre'].lower() == encontrar.lower():  # Comparar en minúsculas
#                 print(f"Contacto encontrado: Nombre: {contacto['Nombre']}, Correo: {contacto['Correo ']}, Teléfono: {contacto['Telefono']}")
#                 encontrado = True
#                 break
#         if not encontrado:
#             print("El nombre que está buscando no está en la agenda.")
#     def Editar(self):
#         nombre = input("Ingrese el nombre del contacto a editar: ")
#         for contacto in self.contactos:
#             if contacto['Nombre'].lower() == nombre.lower():
#                 print("Contacto encontrado.")
#                 nuevo_telefono = input("Ingrese el nuevo teléfono ")
#                 contacto['Telefono']=nuevo_telefono
#                 nuevo_correo = input("Ingrese el nuevo correo: ")
#                 contacto['Correo']=nuevo_correo
#                 print("Contacto editado correctamente.")
#                 return
#         print("Contacto no encontrado.")
#     def Eliminar(self):
#         nombre=input("ingrese el nombre de la persona que desea eliminar: ")
#         for i in self.contactos:
#             if i['Nombre']== nombre:
#                 self.contactos.remove(i)
#                 print("El contacto ha sido eliminado")
#                 break
#             else:
#                 print("el contaccto no existe")
#                 self.Eliminar()
#     def Menu (self) :
#         while True:
#             print("""
#               menu:
#               1.Añadir contactos
#               2.Lista de contactos
#               3.Buscar contactos
#               4.Editar contacos
#               5.Eliminar contactos
#               6.cerrar agenda""")
#             opcion=input("digite una opcion: ")
#             if opcion == "1":
#                 self.Añadir()
#             elif opcion == "2":
#                 self.Lista()
#             elif opcion == "3":
#                 self.Buscar()
#             elif opcion == "4":
#                 self.Editar()
#             elif opcion == "5":
#                 self.Eliminar()
#             elif opcion == "6":
#                 break
#             else:
#                 print("A marcado una opcion erronea")
# Agenda ()
    
import pandas as pd
import re

class Agenda:
    def __init__(self):
        self.contactos = pd.DataFrame(columns=['Nombre', 'Correo', 'Telefono'])
        self.menu()

    def lista(self):
        if self.contactos.empty:
            print("La agenda está vacía.")
        else:
            print(self.contactos)

    def validar_correo(self, correo):
        # Patrón de correo electrónico
        patron = r'^[\w\.-]+@[\w\.-]+\.\w+$'
        return re.match(patron, correo) is not None

    def añadir(self):
        nombre = input("Ingrese el nombre: ")
        correo = input("Ingrese el correo electrónico: ")
        while not self.validar_correo(correo):
            print("Correo no válido, intente nuevamente.")
            correo = input("Ingrese el correo electrónico: ")
        telefono = input("Ingrese el número de teléfono: ")

        nuevo_contacto = pd.DataFrame([[nombre, correo, telefono]], columns=['Nombre', 'Correo', 'Telefono'])
        self.contactos = pd.concat([self.contactos, nuevo_contacto], ignore_index=True)
        print("Contacto guardado")

    def buscar(self):
        nombre = input("Digite el nombre de la persona que quiere buscar: ")
        resultado = self.contactos[self.contactos['Nombre'].str.lower() == nombre.lower()]
        if resultado.empty:
            print("El nombre que está buscando no está en la agenda.")
        else:
            print("Contacto encontrado:")
            print(resultado)

    def editar(self):
        nombre = input("Ingrese el nombre del contacto a editar: ")
        contacto_index = self.contactos[self.contactos['Nombre'].str.lower() == nombre.lower()].index

        if not contacto_index.empty:
            nuevo_telefono = input("Ingrese el nuevo teléfono: ")
            nuevo_correo = input("Ingrese el nuevo correo electrónico: ")
            while not self.validar_correo(nuevo_correo):
                print("Correo no válido, intente nuevamente.")
                nuevo_correo = input("Ingrese el nuevo correo electrónico: ")

            # Actualizar contacto
            self.contactos.loc[contacto_index, 'Correo'] = nuevo_correo
            self.contactos.loc[contacto_index, 'Telefono'] = nuevo_telefono
            print("Contacto editado correctamente.")
        else:
            print("Contacto no encontrado.")

    def eliminar(self):
        nombre = input("Ingrese el nombre de la persona que desea eliminar: ")
        contacto_index = self.contactos[self.contactos['Nombre'].str.lower() == nombre.lower()].index

        if not contacto_index.empty:
            self.contactos = self.contactos.drop(contacto_index)
            print("El contacto ha sido eliminado.")
        else:
            print("El contacto no existe en la agenda.")

    def menu(self):
        while True:
            print("""
              Menú:
              1. Añadir contacto
              2. Lista de contactos
              3. Buscar contacto
              4. Editar contacto
              5. Eliminar contacto
              6. Cerrar agenda""")
            opcion = input("Digite una opción: ")
            if opcion == "1":
                self.añadir()
            elif opcion == "2":
                self.lista()
            elif opcion == "3":
                self.buscar()
            elif opcion == "4":
                self.editar()
            elif opcion == "5":
                self.eliminar()
            elif opcion == "6":
                break
            else:
                print("Ha marcado una opción errónea.")

# Crear una instancia de la clase Agenda
Agenda()

