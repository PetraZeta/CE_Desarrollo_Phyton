# definción d la interfaz

from abc import ABC, abstractmethod


class ICrud(ABC):
    @abstractmethod
    def create(self):
        pass

    @abstractmethod
    def read(self):
        pass

    @abstractmethod
    def update(self):
        pass

    @abstractmethod
    def delete(self):
        pass

    @abstractmethod
    def show(self):
        pass


class Persona:
    def __init__(self, nombre, apellidos, correo):
        self.nombre = nombre
        self.apellidos = apellidos
        self.correo = correo

    def __str__(self):
        return f"Nombre: {self.nombre} {self.apellidos} - Correo: {self.correo}"

    def __eq__(self, other):
        return self.correo == other.correo


class GestionPersonas(ICrud):
    def __init__(self):
        self.personas = []

    def create(self, persona):
        # Agregar persona a la lista
        if persona not in self.personas:
            self.personas.append(persona)
            return True
        return False

    def read(self, correo):
        # Buscar persona por correo
        for persona in self.personas:
            if persona.correo == correo:
                return persona
        return None

    def update(self, correo_persona, nuevo_nombre):
        persona = self.read(correo_persona)
        if persona:
            persona.nombre = nuevo_nombre
            return True
        return False

    def delete(self, correo_persona):
        persona = self.read(correo_persona)
        if persona:
            self.personas.remove(persona)
            return True
        return False

    def show(self):
        for persona in self.personas:
            print(persona)
