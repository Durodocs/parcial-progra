#Hotel-Emilio
class habitacines():#Clase para mostrar las habitaciones
      
      def __init__(self, habitacion1="", habitacion2=""):
          self.habitacion1 = habitacion1
          self.habitacion2 = habitacion2

      def habitacion(self):#muestreo de habitaciones
        self.habitacion1 = "Habitacion grande, $40 la noche" 
        self.habitacion2 = "Habitacion pequeña, $20 la noche"
        print("Bienvenidos al hotel, acontonuación mostras las habitaciones disponibles y sus precios")
        print(self.habitacion1)
        print(self.habitacion2)

class clientes():#Informacion del cliente
    def __init__(self, nombre="", telefono=0, noches=0, habitacion=0):
        self.nombre = nombre
        self.telefono = telefono
        self.noches = noches
        self.habitacion = habitacion

    def ingresar_datos(self):
        self.nombre = input("Ingrese su nombre: ")
        self.telefono = int(input("Ingrese su numero de telefono: "))
        self.noches = int(input("Cuantas noches estar: "))
        self.habitacion = int(input("Que habitacion van a escoger, 1 o 2: "))

    
    def muestreo_datos(self):
        print(f"Nombre del cliente: {self.nombre}")
        print(f"Numero telefonico: {self.telefono}")
        print(f"Noches hospedadas: {self.noches}")
        if self.habitacion == 1:
            print("Usted ha escogido la habitacion de $40 la noche")
            self.op = self.noches * 40
            self.op2 = self.noches * 20

            print(f"Total a pagar: {self.op}")
        else: (f"Noche de $20 la hora")


veri = habitacines()
veri.habitacion()
veri2 = clientes()
veri2.ingresar_datos()
veri2.muestreo_datos()

#Este codigo sencillo para mostrar datos que el cliente ahay elegido
