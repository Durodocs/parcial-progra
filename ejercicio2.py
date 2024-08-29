from datetime import datetime, timedelta

class libro:
    def __init__(self,titulo,autor):
        self.titulo = titulo
        self.autor = autor
        self.disponible = True
    
class usuario :
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





        
        
        
    





        

        

