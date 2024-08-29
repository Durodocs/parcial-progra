from datetime import datetime, timedelta


class Vehiculo:
    def __init__(self, tipo, marca, modelo, coste_por_dia):
        self.tipo = tipo
        self.marca = marca
        self.modelo = modelo
        self.coste_por_dia = coste_por_dia
        self.disponible = True


class Cliente:
    def __init__(self, nombre):
        self.nombre = nombre
        self.vehiculos_rentados = []


class Renta:
    def __init__(self, cliente, vehiculo, fecha_renta, dias_renta):
        self.cliente = cliente
        self.vehiculo = vehiculo
        self.fecha_renta = fecha_renta
        self.fecha_devolucion = fecha_renta + timedelta(days=dias_renta)
        self.coste_total = dias_renta * vehiculo.coste_por_dia
        self.devuelto = False

    def devolver_vehiculo(self):
        self.devuelto = True
        self.vehiculo.disponible = True
        return f"Vehículo devuelto. Coste total de la renta: {self.coste_total:.2f}."

class EmpresaRenta:
    def __init__(self):
        self.vehiculos = []
        self.clientes = []
        self.rentas = []


    def agregar_vehiculo(self, vehiculo):
        self.vehiculos.append(vehiculo)


    def registrar_cliente(self, cliente):
        self.clientes.append(cliente)


    def rentar_vehiculo(self, cliente, vehiculo, dias_renta):
        if vehiculo.disponible:
            fecha_renta = datetime.now()
            renta = Renta(cliente, vehiculo, fecha_renta, dias_renta)
            self.rentas.append(renta)
            cliente.vehiculos_rentados.append(vehiculo)
            vehiculo.disponible = False
            return f"Vehículo '{vehiculo.marca} {vehiculo.modelo}' rentado a {cliente.nombre} por {dias_renta} días."
        else:
            return "El vehículo no está disponible."


    def devolver_vehiculo(self, renta):
        resultado = renta.devolver_vehiculo()
        renta.cliente.vehiculos_rentados.remove(renta.vehiculo)
        return resultado


def mostrar_menu():
    print("\n--- Menú de Renta de Vehículos terrestres---")
    print("1. Agregar vehículo")
    print("2. Registrar cliente")
    print("3. Rentar vehículo")
    print("4. Devolver vehículo")
    print("5. Salir")
    return input("Seleccione una opción:   ")

def main():
    empresa = EmpresaRenta()

    while True:
        opcion = mostrar_menu()
        
        if opcion == "1":

            tipo = input("Ingrese el tipo de vehículo (ej. Auto, Camioneta, Moto): ")
            marca = input("Ingrese la marca del vehículo: ")
            modelo = input("Ingrese el modelo del vehículo: ")
            coste_por_dia = float(input("Ingrese el coste por día de renta: "))
            vehiculo = Vehiculo(tipo, marca, modelo, coste_por_dia)
            empresa.agregar_vehiculo(vehiculo)
            print(f"Vehículo '{marca} {modelo}' agregado al lote.")

        elif opcion == "2":

            nombre = input("Ingrese el nombre del cliente: ")
            cliente = Cliente(nombre)
            empresa.registrar_cliente(cliente)
            print(f"Cliente '{nombre}' registrado en el sistema.")

        elif opcion == "3":

            nombre_cliente = input("Ingrese el nombre del cliente: ")
            tipo_vehiculo = input("Ingrese el tipo de vehículo a rentar: ")


            cliente = next((c for c in empresa.clientes if c.nombre == nombre_cliente), None)
            if cliente is None:
                print("Cliente no encontrado.")
                continue

            vehiculo = next((v for v in empresa.vehiculos if v.tipo == tipo_vehiculo and v.disponible), None)
            if vehiculo is None:
                print("No hay vehículos disponibles de ese tipo.")
                continue


            dias_renta = int(input("Ingrese la cantidad de días para la renta: "))


            resultado = empresa.rentar_vehiculo(cliente, vehiculo, dias_renta)
            print(resultado)

        elif opcion == "4":

            nombre_cliente = input("Ingrese el nombre del cliente: ")
            modelo_vehiculo = input("Ingrese el modelo del vehículo a devolver: ")


            renta = next((r for r in empresa.rentas if r.cliente.nombre == nombre_cliente and r.vehiculo.modelo == modelo_vehiculo and not r.devuelto), None)
            if renta is None:
                print("Renta no encontrada o ya devuelta.")
                continue


            resultado = empresa.devolver_vehiculo(renta)
            print(resultado)

        elif opcion == "5":

            print("Saliendo del programa.")
            break

        else:
            print("Opción no válida, por favor intente nuevamente.")


if __name__ == "__main__":
    main()
