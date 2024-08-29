#Consultorio-Emilio

class Paciente(): #Clase  de paciente
    def __init__(self, nombre="", edad=0, motivo=""):
        self.nombre = nombre
        self.edad = edad
        self.motivo = motivo
    
    def ingresar_datos_paciente(self): #Pedimos al usuario ingresar sus datos
        self.nombre = input("Ingrese su nombre: ")
        self.edad = int(input("Ingrese su edad: "))
        self.motivo = input("Ingrese su motivo: ")
        print("-------------------------------------")

    def muestreo_datos_paciente(self): #Mostramos los datos ingresados por el usuario
        print(f"Nombre del paciente: {self.nombre}")
        print(f"La edad del paciente: {self.edad}")
        print(f"Motivo de la consulta: {self.motivo}")
        print("-------------------------------------")

class Estado_paciente(): #Creamos una nueva clase para determinar el estado del paciente
    def __init__(self, estado=""):
         self.estado = estado

    def ingresar_estado(self): #Determinanos el estado del paciente
        self.estado = (input("Usted tiene consulta previa, si o no: "))
        if self.estado == "Si"|"si": #Mediante una condicion sabremos el estado del paciente
                print("Usted pasa a sala de espera")
        else: print("Excelente, usted tiene nueva fecha de consulta")
        print("-------------------------------------")

veri = Paciente()
veri.ingresar_datos_paciente()
veri.muestreo_datos_paciente()
veri2 = Estado_paciente()
veri2.ingresar_estado()
veri2.mostrar_estado()
             
#Decidi crear este codigo de dicha manera, para hacer un tramite y registro de datos sencillo.


