import csv, os


class Resultadojuego:
    def __init__(self, year, host_country, host_city, country_name, country_code, gold, silver, bronze):
        self.year = int(year)
        self.host_country = host_country
        self.host_city = host_city
        self.country_name = country_name
        self.country_code = country_code
        self.gold = int(gold)
        self.silver = int(silver)
        self.bronze = int(bronze)

    def __str__(self):
        return f"{self.year} - {self.country_name} - {self.gold} - {self.silver} - {self.bronze}"


class GestionJuegos:

    def __init__(self, archivo):
        self.resultados = self.__cargar_resultados(archivo)

    def __cargar_resultados(self, archivo):
        results = []
        lista = self.__leer_archivo(archivo)
        for elemento in lista:
            resultado = Resultadojuego(*elemento)
            results.append(resultado)
        return results

    def __leer_archivo(self, archivo):
        with open(archivo, "r") as archivo:
            lector = csv.reader(archivo)
            cabeceras = next(lector)  # Ignorar cabeceras
            lista = list(lector)
            return lista

    def obtener_datos_pais(self, codigo_pais):
        return [
            resultado
            for resultado in self.resultados
            if resultado.country_code == codigo_pais
        ]

    def total_medallas_pais_juegos(self, codigo_pais, anio_juegos):
        return sum(
            resultado.gold + resultado.silver + resultado.bronze
            for resultado in self.resultados
                if resultado.country_code == codigo_pais and resultado.year == anio_juegos
        )

    def generar_csv(self, codigo_pais):
        absoluta = os.path.abspath(__file__)
        directorio = os.path.dirname(absoluta)
        archivo = os.path.join(directorio, f"{codigo_pais}.csv")
        
        datos_pais = self.obtener_datos_pais(codigo_pais)
        if len(datos_pais) == 0:
            return "No hay datos para el país"
        else:
            with open(archivo, "w", encoding='utf8') as archivo:
                escritor = csv.writer(archivo, delimiter=",", lineterminator="\n")
                escritor.writerow(
                    list(self.resultados[0].__dict__.keys())
                )
                for resultado in datos_pais:                
                    escritor.writerow(
                        list(resultado.__dict__.values())
                    )
            return f"Archivo {codigo_pais}.csv generado"        
