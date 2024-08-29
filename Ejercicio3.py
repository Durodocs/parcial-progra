#Hotel-Emilio
habitacion1 = "Habitacion grande, $40 la noche" 
habitacion2 = "Habitacion pequeña, $20 la noche"
print("Bienvenidos al hotel, acontonuación mostras las habitaciones disponibles y sus precios")
print(habitacion1)
print(habitacion2)

class clientes():
    def __init__(self, nombre="", telefono=0, noches=0):
        self.nombre = nombre
        self.telefono = telefono
        self.noches = noches

    def ingresar_datos(self):
        self.nombre = input("Ingrese su nombre: ")
        self.telefono = int(input())

    