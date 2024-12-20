class Movie:

    def __init__(self, title, year, director, cast, genre, minutes, producer):
        self.title = title
        self.year = year
        self.director = director
        self.cast = cast
        self.genre = genre
        self.minutes = minutes
        self.producer = producer

    def __str__(self):
        return f"{self.title} - {self.minutes} - {self.producer}"
    
    
class ListMovies:

    list_movies = [
            Movie("The Shawshank Redemption", 1994, "Frank Darabont", "Tim Robbins, Morgan Freeman", "Drama", 142, "Castle Rock Entertainment"),
            Movie("The Godfather", 1972, "Francis Ford Coppola", "Marlon Brando, Al Pacino", "Drama", 175, "Paramount Pictures"),
            Movie("The Dark Knight", 2008, "Christopher Nolan", "Christian Bale, Heath Ledger", "Action", 152, "Warner Bros. Pictures"),
            Movie("The Lord of the Rings: The Return of the King", 2003, "Peter Jackson", "Elijah Wood, Viggo Mortensen", "Adventure", 201, "New Line Cinema"),
            Movie("Pulp Fiction", 1994, "Quentin Tarantino", "John Travolta, Uma Thurman", "Crime", 154, "Miramax Films"),
            Movie("Forrest Gump", 1994, "Robert Zemeckis", "Tom Hanks, Robin Wright", "Drama", 142, "Paramount Pictures"),
            Movie("Inception", 2010, "Christopher Nolan", "Leonardo DiCaprio, Joseph Gordon-Levitt", "Action", 148, "Warner Bros. Pictures"),
            Movie("The Matrix", 1999, "Lana Wachowski, Lilly Wachowski", "Keanu Reeves, Laurence Fishburne", "Action", 136, "Warner Bros. Pictures"),
            Movie("The Silence of the Lambs", 1991, "Jonathan Demme", "Jodie Foster, Anthony Hopkins", "Crime", 118, "Orion Pictures"),
            Movie("The Departed", 2006, "Martin Scorsese", "Leonardo DiCaprio, Matt Damon", "Crime", 151, "Warner Bros. Pictures"),
            Movie("The Prestige", 2006, "Christopher Nolan", "Christian Bale, Hugh Jackman", "Drama", 130, "Warner Bros. Pictures"),
            Movie("The Green Mile", 1999, "Frank Darabont", "Tom Hanks, Michael Clarke Duncan", "Drama", 189, "Castle Rock Entertainment"),
            Movie("The Godfather: Part II", 1974, "Francis Ford Coppola", "Al Pacino, Robert De Niro", "Drama", 202, "Paramount Pictures"),
            Movie("The Lord of the Rings: The Fellowship of the Ring", 2001, "Peter Jackson", "Elijah Wood, Ian McKellen", "Adventure", 178, "New Line Cinema"),
            Movie("The Lord of the Rings: The Two Towers", 2002, "Peter Jackson", "Elijah Wood, Viggo Mortensen", "Adventure", 179, "New Line Cinema"),
            Movie("The Dark Knight Rises", 2012, "Christopher Nolan", "Christian Bale, Tom Hardy", "Action", 164, "Warner Bros. Pictures"),
            Movie("The Lord of the Rings: The Two Towers", 2002, "Peter Jackson", "Elijah Wood, Viggo Mortensen", "Adventure", 179, "New Line Cinema"),
            Movie("One Flew Over the Cuckoo's Nest", 1975, "Milos Forman", "Jack Nicholson, Louise Fletcher", "Drama", 133, "Fantasy Films"),
            Movie("Goodfellas", 1990, "Martin Scorsese", "Robert De Niro, Ray Liotta", "Crime", 146, "Warner Bros. Pictures")
    ]


    # Retornar las pelis de una productora pasada como parámetro.
    @classmethod
    def movies_producer(cls, producer):
        # return [movie for movie in cls.list_movies if movie.producer.lower() == producer.lower()]
        lista = []
        for movie in cls.list_movies:
            if movie.producer.lower() == producer.lower():
                lista.append(movie)

        return lista


    # Retornar las pelis con una cadena en el título. Esta cadena se pasará como parámetro.
    @classmethod
    def movies_string(cls, string):
        return [movie for movie in cls.list_movies if string in movie.title]

    # Retornar cuántas pelis superan la duración media.
    @classmethod
    def minutes_greater_avg(cls):        
        avg = cls.avg_minutes()
        return len([movie for movie in cls.list_movies if movie.minutes > avg]) 
        
    @classmethod
    def avg_minutes(cls):
        minutes = [movie.minutes for movie in cls.list_movies]
        avg_minutes = sum(minutes) / len(minutes)
        return avg_minutes

    # Ordenar por el campo duración. 
    @classmethod
    def sort_by_minutes(cls, rev):
        cls.list_movies.sort(key=lambda movie: movie.title, reverse=rev)
        

    # mostrar pelis
    @classmethod
    def show_movies(cls):
        print(*cls.list_movies, sep="\n")