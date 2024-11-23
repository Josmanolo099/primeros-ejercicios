import datetime

carros_ingresados = 0
motos_ingresadas = 0
dinero_recolectado = 0
vehiculos = {}
def registrar_vehiculo():
    global carros_ingresados, motos_ingresadas
    while True:
        tipo = input("Ingrese el tipo de vehículo (carro/moto): ").lower()
        if tipo == "carro" or tipo == "moto":
            break
        else:
            print("Tipo de vehículo inválido. Solo se permite 'carro' o 'moto'.")
    placa = input("Ingrese la placa del vehículo: ")
    hora_entrada = input("Ingrese la hora de entrada (HH:MM): ")
    vehiculos[placa] = {
        'tipo': tipo,
        'entrada': hora_entrada,
        'salida': None,
        'duracion': None,
        'cobro': None
    }
    if tipo == 'carro':
        carros_ingresados += 1
    elif tipo == 'moto':
        motos_ingresadas += 1
    print(f"Vehículo {tipo} con placa {placa} registrado a las {hora_entrada}.")
def registrar_salida():
    global dinero_recolectado
    placa = input("Ingrese la placa del vehículo que sale: ")
    
    salida = input("Ingrese la hora de salida (HH:MM): ")
    vehiculos[placa]['salida'] = salida
    
    hora_entrada = datetime.datetime.strptime(vehiculos[placa]["entrada"], "%H:%M")
    hora_salida_dt = datetime.datetime.strptime(salida, "%H:%M")
    duracion = int((hora_salida_dt - hora_entrada).total_seconds() // 60)
    
    # Calcular la duración en minutos
    #duracion = (hora_salida - hora_entrada).total_seconds() // 60
    vehiculos[placa]['duracion'] = duracion
    
    
    if vehiculos[placa]['tipo'] == 'carro':
        cobro = ((duracion // 15) + 1) * 1000
    else:
        cobro = ((duracion // 15) + 1) * 500
    
    vehiculos[placa]['cobro'] = cobro
    dinero_recolectado += cobro
    
    print(f"Duración: {duracion} minutos. Total a pagar: ${cobro}")


def mostrar_resumen():
    print(f"Carros ingresados: {carros_ingresados}")
    print(f"Motos ingresadas: {motos_ingresadas}")
    print(f"Dinero recolectado: ${dinero_recolectado}")
def menu():
    while True:
        
        print ("""\n Menú
                   1. Registrar vehículo
                   2. Registrar salida de vehículo
                   3. Mostrar resumen del día
                   4. salir""")
        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            registrar_vehiculo()
        elif opcion == "2":
            registrar_salida()
        elif opcion == "3":
            mostrar_resumen()
        elif opcion == "4":
            break
        else:
            print("Opción no válida. Intente de nuevo.")
            menu()
menu()