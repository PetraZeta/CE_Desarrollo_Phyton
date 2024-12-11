from clases import *

# contacto_buscado = Agenda.buscar_contacto("Ana")
# print(contacto_buscado)

# nombre_contacto = "Anaddddddd"
# telefono = Agenda.telefono_de_contacto(nombre_contacto)
# if not telefono:   #ha devuelto None
#     print(f"No existe contacto {nombre_contacto}")
# else:
#     print(f"Teléfono de {nombre_contacto}: {telefono}")

#print(Agenda.correo_de_contacto("ana54545454"))

# Agenda.cambiar_telefono_contacto("Ana", "924000001")
# Agenda.cambiar_correo_contacto("Ana", "ana@movistar.com")

# contacto_buscado = Agenda.buscar_contacto("Ana")
# print(contacto_buscado)

Agenda.listar_contactos()

numero_contactos = Agenda.contar_contactos()
print(f"Nº de contactos en agenda: {numero_contactos}")