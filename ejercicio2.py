from datetime import datetime, timedelta


class Libro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor
        self.disponible = True


class Usuario:
    def __init__(self, nombre):
        self.nombre = nombre
        self.libros_prestados = []


class Prestamo:
    def __init__(self, usuario, libro, fecha_prestamo, dias_prestamo=14):
        self.usuario = usuario
        self.libro = libro
        self.fecha_prestamo = fecha_prestamo
        self.fecha_limite = fecha_prestamo + timedelta(days=dias_prestamo)
        self.devuelto = False


    def devolver_libro(self):
        self.devuelto = True
        self.libro.disponible = True
        fecha_devolucion = datetime.now()
        if fecha_devolucion > self.fecha_limite:
            dias_tarde = (fecha_devolucion - self.fecha_limite).days
            return f"Libro devuelto con {dias_tarde} días de retraso. Sanción aplicada."
        return "Libro devuelto a tiempo. Gracias."


class Biblioteca:
    def __init__(self):
        self.libros = []
        self.usuarios = []
        self.prestamos = []


    def agregar_libro(self, libro):
        self.libros.append(libro)

    def registrar_usuario(self, usuario):
        self.usuarios.append(usuario)


    def prestar_libro(self, usuario, libro):
        if libro.disponible:
            fecha_prestamo = datetime.now()
            prestamo = Prestamo(usuario, libro, fecha_prestamo)
            self.prestamos.append(prestamo)
            usuario.libros_prestados.append(libro)
            libro.disponible = False
            return f"Libro '{libro.titulo}' prestado a {usuario.nombre} hasta {prestamo.fecha_limite.date()}."
        else:
            return "El libro no está disponible."


    def devolver_libro(self, prestamo):
        resultado = prestamo.devolver_libro()
        prestamo.usuario.libros_prestados.remove(prestamo.libro)
        return resultado


def mostrar_menu():
    print("\n--- Menú de la Biblioteca ---")
    print("1. Agregar libro")
    print("2. Registrar usuario")
    print("3. Prestar libro")
    print("4. Devolver libro")
    print("5. Salir")
    return input("Seleccione una opción: ")

def main():
    biblioteca = Biblioteca()

    while True:
        opcion = mostrar_menu()
        
        if opcion == "1":
            titulo = input("Ingrese el título del libro: ")
            autor = input("Ingrese el autor del libro: ")
            libro = Libro(titulo, autor)
            biblioteca.agregar_libro(libro)
            print(f"Libro '{titulo}' de {autor} agregado a la biblioteca.")

        elif opcion == "2":

            nombre = input("Ingrese el nombre del usuario: ")
            usuario = Usuario(nombre)
            biblioteca.registrar_usuario(usuario)
            print(f"Usuario '{nombre}' registrado en la biblioteca.")

        elif opcion == "3":

            nombre_usuario = input("Ingrese el nombre del usuario: ")
            titulo_libro = input("Ingrese el título del libro: ")

            usuario = next((u for u in biblioteca.usuarios if u.nombre == nombre_usuario), None)
            if usuario is None:
                print("Usuario no encontrado.")
                continue

            libro = next((l for l in biblioteca.libros if l.titulo == titulo_libro), None)
            if libro is None:
                print("Libro no encontrado.")
                continue


            resultado = biblioteca.prestar_libro(usuario, libro)
            print(resultado)

        elif opcion == "4":

            nombre_usuario = input("Ingrese el nombre del usuario: ")
            titulo_libro = input("Ingrese el título del libro a devolver: ")

            prestamo = next((p for p in biblioteca.prestamos if p.usuario.nombre == nombre_usuario and p.libro.titulo == titulo_libro and not p.devuelto), None)
            if prestamo is None:
                print("Préstamo no encontrado o ya devuelto.")
                continue


            resultado = biblioteca.devolver_libro(prestamo)
            print(resultado)

        elif opcion == "5":

            print("Saliendo del programa.")
            break

        else:
            print("Opción no válida, por favor intente nuevamente.")

if __name__ == "__main__":
    main()

    








        
        
        
    





        

        

