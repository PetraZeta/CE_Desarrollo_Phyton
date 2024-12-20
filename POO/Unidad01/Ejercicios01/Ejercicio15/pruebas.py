from clases import Ciudad, ListaCiudades


ciudades_australia = ListaCiudades.ciudades_pais("Australia")

for ciudad in ciudades_australia:
    print(ciudad)

ciudades_aus = ListaCiudades.ciudades_pais("Australia")

print(*ciudades_aus)

# # nueva =  Ciudad("Lima", 10000000, "Peru", "America")
# # result = ListaCiudades.anadir_ciudad(nueva)
# # print(result)

# media_hab_australia = ListaCiudades.media_poblacion_ciudades_pais("Australiaasdfasdfasdf")
# print(media_hab_australia)

# cuenta = ListaCiudades.contar_ciudades_pais("Australia")
# print(cuenta)

# cuenta = ListaCiudades.contar_ciudades_cadena("an")
# print(cuenta)