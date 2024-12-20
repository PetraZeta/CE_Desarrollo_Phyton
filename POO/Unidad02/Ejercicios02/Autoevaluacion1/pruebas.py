from clases import *

# lista de objetos Persona
personas = [
    Cliente('Juan', 'Perez', 'juan@gmail.com', 1, '1234567890'),
    Trabajador('Maria', 'Lopez', 'maria@gamil.com', 1, 1000),
    Trabajador('Pedro', 'Gomez', 'pedro@ggg.com', 2, 2000),
    Cliente('Ana', 'Martinez', 'ana@hotdog.es', 2, '0987654321'),
    Cliente('Luis', 'Garcia', 'lliss@nomore.com' , 3, '1234567890')
]


# Todos los objetos son instancias de la clase Persona
# ya que Cliente y Trabajador son subclases de Persona
for persona in personas:
    if isinstance(persona, Persona):
        print(f'{persona.nombre} {persona.apellidos} - {persona.correo}, es un cliente')