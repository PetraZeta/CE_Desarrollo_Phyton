import collections, csv, json, os


class Partido:
    def __init__(self, jornada, fecha, local, visitante, goles_local, goles_visitante, total_goles, ganador):
        self.jornada = jornada
        self.fecha = fecha
        self.local = local
        self.visitante = visitante
        self.goles_local = goles_local
        self.goles_visitante = goles_visitante
        self.total_goles = total_goles
        self.ganador = ganador

    def __str__(self):
        return f'Jornada: {self.jornada}, Fecha: {self.fecha}' \
            f' {self.local} {self.goles_local} - {self.goles_visitante} ' \
            f'{self.visitante}'
    


class ColeccionPartidos:
    
    def __init__(self, archivo):
        self.partidos = self.__cargar_partidos(archivo)
        self.cabeceras = None

    def __cargar_partidos(self, archivo):
        with open(archivo, 'r', encoding='utf-8') as csv_file:
            csv_reader = csv.reader(csv_file)
            self.cabeceras = list(next(csv_reader))
            partidos = []
            for linea in csv_reader:
                jornada = int(linea[0])
                fecha = linea[1]
                local = linea[2]
                visitante = linea[3]
                goles_local = int(linea[4])
                goles_visitante = int(linea[5])
                total_goles = goles_local + goles_visitante
                ganador = local if goles_local > goles_visitante else visitante if goles_visitante > goles_local else 'Empate'
                partido = Partido(jornada, fecha, local, visitante, goles_local, goles_visitante, total_goles, ganador)
                partidos.append(partido)
        return partidos
        
    def csv_partidos_local(self, equipo):
        partidos_local = [partido for partido in self.partidos if partido.local.lower() == equipo.lower()]
        print(len(partidos_local))
        archivo = os.path.join(os.path.dirname(__file__), f'{equipo}_local.csv')
        try:
            with open(archivo, 'w', encoding='utf-8') as csv_file:
                # ordenar por jornada                
                partidos_local.sort(key= lambda p: p.jornada)
                csv_writer = csv.writer(csv_file, delimiter=',', lineterminator='\n')
                csv_writer.writerow(partidos_local[0].__dict__.keys())
                for partido in partidos_local:
                    csv_writer.writerow([partido.jornada, partido.fecha, partido.local, partido.visitante, 
                        partido.goles_local, partido.goles_visitante, partido.total_goles, partido.ganador])
                
            return True
        except Exception as e:
            return e    
    
    def json_partidos_equipo(self, equipo):
        partidos_local = [partido for partido in self.partidos if partido.local.lower() == equipo.lower()
                        or partido.visitante.lower() == equipo.lower()]
        
        archivo = os.path.join(os.path.dirname(__file__), f'{equipo}_2324.json')
        try:
            with open(archivo, 'w', encoding='utf-8') as json_file:
                partidos_json = {partido.jornada: partido.__dict__ for partido in partidos_local}
                json.dump(partidos_json, json_file, indent=4)
            return True
        except Exception as e:
            return e


    def csv_clasificacion(self):
        
        dict_clasificacion = collections.defaultdict(int)
        for partido in self.partidos:
            puntos_local = 0; puntos_visitante = 0
            if partido.ganador == 'Empate':
                puntos_local = 1
                puntos_visitante = 1
            elif partido.ganador == partido.local:
                puntos_local = 3
            else:
                puntos_visitante = 3

            dict_clasificacion[partido.local] += puntos_local
            dict_clasificacion[partido.visitante] += puntos_visitante
       
        dict_clasificacion = dict(sorted(dict_clasificacion.items(), key= lambda x: x[1], reverse=True))
        
        try:
            archivo = os.path.join(os.path.dirname(__file__), 'clasificacion_liga_2324.csv')
            with open(archivo, 'w', encoding='utf8') as clasi_csv:
                csv_writer = csv.writer(clasi_csv, delimiter=',', lineterminator='\n')
                csv_writer.writerow(['Posición','Equipo', 'Puntos'])
                posicion = 1
                for equipo, puntos in dict_clasificacion.items():
                    csv_writer.writerow([posicion, equipo, puntos])
                    posicion += 1
            return True
        except:        
            return True
                



        
