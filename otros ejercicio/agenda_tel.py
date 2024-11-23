#Diseñe un algoritmo e impleméntelo con Python para resolver sistemas 
# de ecuaciones lineales 2x2. Su programa debe recibir los coeficientes de las 2 ecuaciones, 
# verificar si tiene solución y mostrar el resultado de sus raíces.
# def Resolv_ecu (a1,a2,b1,b2,c1,c2):
#     d=(a1*b2)-(a2*b1)
#     if d==0:
#         print("el sistema tiene infinitas soluciones o no tiene soluciones")
#     else:
#         dx=((c1*b2)-(c2*b1))/d
#         dy=((a1*c2)-(a2*c1))/d
#         print("la suluciones para la ecuacion es en X= ",dx," y para Y= ",dy)

# print("""SISTEMA DE ECUACIONES 2X2
#        PRIMERA ECUACION""")
# x=int(input("Diguite el numero que acompaña a la x "))
# y=int(input("Diguite el numero que acompaña a la y "))
# r=int(input("Diguite el valor que esta despues del igual "))
# print("SEGUNDA ECUACION")
# x1=int(input("Diguite el numero que acompaña a la x "))
# y1=int(input("Diguite el numero que acompaña a la y "))
# r2=int(input("Diguite el valor que esta despues del igual "))
# Resolv_ecu (x,x1,y,y1,r,r2)

def main():
    agenda = {}  # Diccionario para almacenar los contactos

    while True:
        print("\n--- AGENDA TELEFÓNICA ---")
        print("1. Agregar contacto")
        print("2. Editar contacto")
        print("3. Eliminar contacto")
        print("4. Mostrar contactos")
        print("5. Salir")

        opcion = input("Selecciona una opción (1-5): ")

        if opcion == "1":
            agregar_contacto(agenda)
        elif opcion == "2":
            editar_contacto(agenda)
        elif opcion == "3":
            eliminar_contacto(agenda)
        elif opcion == "4":
            mostrar_contactos(agenda)
        elif opcion == "5":
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida. Inténtalo de nuevo.")

def agregar_contacto(agenda):
    nombre = input("Nombre completo: ")
    telefono = input("Número de teléfono: ")
    correo = input("Correo electrónico: ")
    direccion = input("Dirección de residencia: ")
    cumpleanos = input("Fecha de cumpleaños (DD/MM): ")

    agenda[nombre] = {
        "Teléfono": telefono,
        "Correo": correo,
        "Dirección": direccion,
        "Cumpleaños": cumpleanos
    }
    print(f"Contacto de {nombre} agregado correctamente.")

def editar_contacto(agenda):
    nombre = input("Nombre del contacto a editar: ")
    if nombre in agenda:
        print(f"Editando información de {nombre}:")
        telefono = input("Nuevo número de teléfono: ")
        correo = input("Nuevo correo electrónico: ")
        direccion = input("Nueva dirección de residencia: ")
        cumpleanos = input("Nueva fecha de cumpleaños (DD/MM): ")

        agenda[nombre]["Teléfono"] = telefono
        agenda[nombre]["Correo"] = correo
        agenda[nombre]["Dirección"] = direccion
        agenda[nombre]["Cumpleaños"] = cumpleanos
        print(f"Información de {nombre} actualizada correctamente.")
    else:
        print(f"{nombre} no está en la agenda.")

def eliminar_contacto(agenda):
    nombre = input("Nombre del contacto a eliminar: ")
    if nombre in agenda:
        del agenda[nombre]
        print(f"Contacto de {nombre} eliminado correctamente.")
    else:
        print(f"{nombre} no está en la agenda.")

def mostrar_contactos(agenda):
    print("\n--- LISTA DE CONTACTOS ---")
    for nombre, info in agenda.items():
        print(f"{nombre}:")
        print(f"  Teléfono: {info['Teléfono']}")
        print(f"  Correo: {info['Correo']}")
        print(f"  Dirección: {info['Dirección']}")
        print(f"  Cumpleaños: {info['Cumpleaños']}")
        print("-" * 30)

if __name__ == "__main__":
    main()
