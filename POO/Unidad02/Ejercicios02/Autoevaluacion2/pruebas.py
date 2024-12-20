from clases import *

gestion = GestionPersonas()

gestion.create(Persona("Juan", "Perez", "jua@ggg.com"))
gestion.create(Persona("Ana", "Masa", "ana@goli.com"))
gestion.create(Persona("Gema", "Brisa", "gema@hotmail.com"))
gestion.create(
    Persona("Gema", "Brisa", "gema@hotmail.com")
)  # Solo añade 1 vez. No repite correo

print(gestion.read("ana@goli.com"))  # busca x correo: Retorna el objeto.
print(gestion.read("ana333@goli.com"))  # busca x correo: retorna None

print(gestion.delete("ana@goli.com"))  # Elimina la persona. Retorna True
print(gestion.delete("ana@goli.com"))  # Eliminar. Retorna False

gestion.update("jua@ggg.com", "Juanito")  # Actualiza el nombre de la persona

gestion.show()  # Muestra los objetos restantes
