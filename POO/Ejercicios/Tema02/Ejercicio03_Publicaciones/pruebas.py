from datetime import date

from clases import *

# Listar libros
ListaPublicaciones.mostrar_publicaciones_libro()

# Contar las publicaciones de tipo "Revista"
result = ListaPublicaciones.contar_publicaciones_tipo("Revista")
print(result)

# Obtener lista de revistas
revistas = ListaPublicaciones.lista_de_revistas()
print(*revistas, sep="\n")

# Contar publicaciones por tipo en diccionario
d = ListaPublicaciones.cuenta_por_tipo()
print(d)

# Obtener tupla de idiomas
idiomas = ListaPublicaciones.tupla_idiomas()
print(idiomas)


for publi in ListaPublicaciones.publicaciones:
    print(publi)