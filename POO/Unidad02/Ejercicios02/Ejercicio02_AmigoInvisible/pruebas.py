from clases import * 
from datetime import date

juego = AmigoInvisible('Fin de año', date(2024,12,12))
juego.anadir_persona('Ana', 'ana@gmail.com')
juego.anadir_persona('Luis', 'luis@gmail.com')
juego.anadir_persona('Gema', 'gema@gmail.com')
juego.anadir_persona('Laura', 'Laura@gmail.com')
print(juego.anadir_persona('Laura', 'Laura@gmail.com'))  # debe retornar False



parejas = juego.sortear()

print("Parejas creadas", parejas, sep="\n")