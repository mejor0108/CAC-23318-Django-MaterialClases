from abc import ABC, abstractmethod


class Persona(ABC):

    def __init__(self,nombre,apellido,dni,email):
        self.nombre = nombre
        self.apellido = apellido
        self.dni = dni
        self.email = email
    
    def __str__(self):
        return f'{self.apellido}, {self.nombre}'


    @abstractmethod
    def registrarse(self):
        pass


class Estudiante(Persona):

    def __init__(self, nombre, apellido, dni, email,matricula):
        super().__init__(nombre, apellido, dni, email)
        self.matricula = matricula

    def registrarse(self):
        return f'El estudiante {self.apellido} se registro exitosamente'
    

class Docente(Persona):

    def __init__(self, nombre, apellido, dni, email,legajo):
        super().__init__(nombre, apellido, dni, email)
        self.legajo = legajo
    
    def registrarse(self):
        return f'Docente registrado con exito!'
    

estudiante_uno = Estudiante('Pepe','Argento',34111222,'pepe@gmail.com','LM-2333')
print(estudiante_uno.registrarse())

docente_uno = Docente('Mony','Argento',3434333,'moni@gmail.com','DC23232')
print(docente_uno.registrarse())
