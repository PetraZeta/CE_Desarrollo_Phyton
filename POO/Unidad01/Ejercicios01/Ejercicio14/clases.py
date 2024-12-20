# Clases Contacto y Agenda

class Contacto:
    def __init__(self, nombre, telefono, correo):
        self.nombre = nombre
        self.telefono = telefono
        self.correo = correo

    def __str__(self):
        return f"{self.nombre}-{self.telefono}-{self.correo}"
    
    def __repr__(self):
        return f"Contacto({self.nombre}, {self.telefono}, {self.correo})"
    
    def __eq__(self, otro_contacto):
        return self.nombre == otro_contacto.nombre and \
            self.telefono == otro_contacto.telefono and \
            self.correo == otro_contacto.correo
    
#################################################################
#################################################################
#################################################################

class Agenda:
    contactos = [1,
        Contacto("Ana", "484484844", "ana@gmail.com"),
        Contacto("Luis", "22222222", "luis@gmail.com"),
        Contacto("Eva", "33333333", "eva@gmail.com"),
        Contacto("Fran", "55555555", "fran@gmail.com"),
        Contacto("Elena", "924556677", "elena@gmail.com"),
    ]

# Buscar contacto por nombre y retornar el contacto.
# Obtener el teléfono de un contacto. Retornar el teléfono.
# Obtener el correo de un contacto. Retornar el correo.
# Cambiar el teléfono de un contacto. Retornar True si se pudo hacer el cambio, False en caso contrario.
# Cambiar el correo de un contacto. Retornar True si se pudo hacer el cambio, False en caso contrario.
# Listar todos los contactos.
# Obtener el número de contactos.

    @classmethod
    def buscar_contacto(cls, nombre_buscado):
        for contacto in cls.contactos:
            if nombre_buscado.lower() == contacto.nombre.lower():
                return contacto
        return None

    @classmethod
    def telefono_de_contacto(cls, nombre_buscado):
        contacto = cls.buscar_contacto(nombre_buscado)
        if contacto:    # el contacto existe?
            return contacto.telefono
        else:
            return None
        
    @classmethod
    def correo_de_contacto(cls, nombre_buscado):
        contacto = cls.buscar_contacto(nombre_buscado)
        if contacto:    # el contacto existe?
            return contacto.correo
        else:
            return None

    @classmethod
    def cambiar_telefono_contacto(cls, nombre_contacto, nuevo_telefono):
        contacto = cls.buscar_contacto(nombre_contacto)
        if contacto:  # Existe contacto?
            contacto.telefono = nuevo_telefono
            return True   # cambio hecho
        else:
            return False  # no existe contacto. No cambio

    @classmethod
    def cambiar_correo_contacto(cls, nombre_contacto, nuevo_correo):
        contacto = cls.buscar_contacto(nombre_contacto)
        if contacto:  # Existe contacto?
            contacto.correo = nuevo_correo
            return True   # cambio hecho
        else:
            return False  # no existe contacto. No cambio
        
    @classmethod
    def listar_contactos(cls):
        for contacto in cls.contactos:
            print(contacto)

    @classmethod
    def contar_contactos(cls):
        return len(cls.contactos)