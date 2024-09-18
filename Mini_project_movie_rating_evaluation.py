# Creating a dataset with a list of dictionaries each dictoinary contain keys as same atributes and values respective to them are unique for each dictionary
movies = [
    {"name": "The Shawshank Redemption", "year": 1994, "genre": "Drama", "rating": 9.3, "director": "Frank Darabont"},
    {"name": "The Godfather", "year": 1972, "genre": "Crime", "rating": 9.2, "director": "Francis Ford Coppola"},
    {"name": "The Dark Knight", "year": 2008, "genre": "Action", "rating": 9.0, "director": "Christopher Nolan"},
    {"name": "12 Angry Men", "year": 1957, "genre": "Drama", "rating": 8.9, "director": "Sidney Lumet"},
    {"name": "Schindler's List", "year": 1993, "genre": "Biography", "rating": 8.9, "director": "Steven Spielberg"},
    {"name": "Pulp Fiction", "year": 1994, "genre": "Crime", "rating": 8.9, "director": "Quentin Tarantino"},
    {"name": "Inception", "year": 2010, "genre": "Sci-Fi", "rating": 8.8, "director": "Christopher Nolan"},
    {"name": "Fight Club", "year": 1999, "genre": "Drama", "rating": 8.8, "director": "David Fincher"},
    {"name": "Forrest Gump", "year": 1994, "genre": "Drama", "rating": 8.8, "director": "Robert Zemeckis"},
    {"name": "The Matrix", "year": 1999, "genre": "Sci-Fi", "rating": 8.7, "director": "The Wachowskis"},
    {"name": "Goodfellas", "year": 1990, "genre": "Crime", "rating": 8.7, "director": "Martin Scorsese"},
    {"name": "The Empire Strikes Back", "year": 1980, "genre": "Sci-Fi", "rating": 8.7, "director": "Irvin Kershner"},
    {"name": "One Flew Over the Cuckoo's Nest", "year": 1975, "genre": "Drama", "rating": 8.7, "director": "Miloš Forman"},
    {"name": "Parasite", "year": 2019, "genre": "Thriller", "rating": 8.6, "director": "Bong Joon Ho"},
    {"name": "Interstellar", "year": 2014, "genre": "Sci-Fi", "rating": 8.6, "director": "Christopher Nolan"},
    {"name": "City of God", "year": 2002, "genre": "Crime", "rating": 8.6, "director": "Fernando Meirelles"},
    {"name": "Spirited Away", "year": 2001, "genre": "Animation", "rating": 8.6, "director": "Hayao Miyazaki"},
    {"name": "Saving Private Ryan", "year": 1998, "genre": "War", "rating": 8.6, "director": "Steven Spielberg"},
    {"name": "The Green Mile", "year": 1999, "genre": "Drama", "rating": 8.6, "director": "Frank Darabont"},
    {"name": "The Usual Suspects", "year": 1995, "genre": "Mystery", "rating": 8.5, "director": "Bryan Singer"},
    {"name": "The Silence of the Lambs", "year": 1991, "genre": "Thriller", "rating": 8.6, "director": "Jonathan Demme"},
    {"name": "Se7en", "year": 1995, "genre": "Thriller", "rating": 8.6, "director": "David Fincher"},
    {"name": "It's a Wonderful Life", "year": 1946, "genre": "Drama", "rating": 8.6, "director": "Frank Capra"},
    {"name": "Life Is Beautiful", "year": 1997, "genre": "Comedy", "rating": 8.6, "director": "Roberto Benigni"},
    {"name": "The Departed", "year": 2006, "genre": "Crime", "rating": 8.5, "director": "Martin Scorsese"},
    {"name": "Gladiator", "year": 2000, "genre": "Action", "rating": 8.5, "director": "Ridley Scott"},
    {"name": "The Prestige", "year": 2006, "genre": "Drama", "rating": 8.5, "director": "Christopher Nolan"},
    {"name": "The Lion King", "year": 1994, "genre": "Animation", "rating": 8.5, "director": "Roger Allers"},
    {"name": "Apocalypse Now", "year": 1979, "genre": "War", "rating": 8.4, "director": "Francis Ford Coppola"},
    {"name": "The Shining", "year": 1980, "genre": "Horror", "rating": 8.4, "director": "Stanley Kubrick"},
    {"name": "Whiplash", "year": 2014, "genre": "Drama", "rating": 8.5, "director": "Damien Chazelle"},
    {"name": "The Great Dictator", "year": 1940, "genre": "Comedy", "rating": 8.4, "director": "Charlie Chaplin"},
    {"name": "The Wolf of Wall Street", "year": 2013, "genre": "Biography", "rating": 8.2, "director": "Martin Scorsese"},
    {"name": "Django Unchained", "year": 2012, "genre": "Western", "rating": 8.4, "director": "Quentin Tarantino"},
    {"name": "Mad Max: Fury Road", "year": 2015, "genre": "Action", "rating": 8.1, "director": "George Miller"},
    {"name": "Braveheart", "year": 1995, "genre": "Biography", "rating": 8.3, "director": "Mel Gibson"},
    {"name": "Alien", "year": 1979, "genre": "Sci-Fi", "rating": 8.4, "director": "Ridley Scott"},
    {"name": "Toy Story", "year": 1995, "genre": "Animation", "rating": 8.3, "director": "John Lasseter"},
    {"name": "Memento", "year": 2000, "genre": "Mystery", "rating": 8.4, "director": "Christopher Nolan"},
    {"name": "The Truman Show", "year": 1998, "genre": "Comedy", "rating": 8.1, "director": "Peter Weir"},
    {"name": "Jaws", "year": 1975, "genre": "Thriller", "rating": 8.0, "director": "Steven Spielberg"},
    {"name": "Raging Bull", "year": 1980, "genre": "Biography", "rating": 8.2, "director": "Martin Scorsese"},
    {"name": "Casablanca", "year": 1942, "genre": "Romance", "rating": 8.5, "director": "Michael Curtiz"},
    {"name": "Raiders of the Lost Ark", "year": 1981, "genre": "Adventure", "rating": 8.4, "director": "Steven Spielberg"},
    {"name": "Amélie", "year": 2001, "genre": "Comedy", "rating": 8.3, "director": "Jean-Pierre Jeunet"},
    {"name": "A Beautiful Mind", "year": 2001, "genre": "Biography", "rating": 8.2, "director": "Ron Howard"},
    {"name": "The Sixth Sense", "year": 1999, "genre": "Mystery", "rating": 8.1, "director": "M. Night Shyamalan"},
    {"name": "WALL·E", "year": 2008, "genre": "Animation", "rating": 8.4, "director": "Andrew Stanton"},
]

# Functions defination
def firstNMovies(movies, n):
    print(movies[:n])

def totalMovies(movies):
    print(f"Total: {len(movies)}")
     
def highestRatedMovie(movies):
    highest_rated_movie = movies[0]
    for movie in movies:
        if movie["rating"] > highest_rated_movie["rating"]:
            highest_rated_movie = movie
    print("Highest:", highest_rated_movie["name"], "(", highest_rated_movie["rating"], ")")
     


def s(movies):
    totalRating = 0
    for movie in movies:
        totalRating += movie["rating"]
    avg_rating = totalRating / len(movies)
    print("Average Rating:", round(avg_rating, 2))
    


def pre200Movies(movies):
    pre_2000 = []
    for movie in movies:
        if movie["year"] < 2000:
            pre_2000.append(movie["name"])
        movie_list = ", ".join(pre_2000)
    print("Before 2000:", movie_list)
        


def highRatedMovies(movies, min=8.0):
    high_rated = []
    for movie in movies:
        if movie["rating"] > min:
            high_rated.append(movie["name"])
        movie_list = ", ".join(high_rated)
    print("Above", min, ":", movie_list)
        


def genreCount(movies):
    genre_count = {}
    for movie in movies:
        genre = movie["genre"]
        if genre in genre_count:
            genre_count[genre] += 1
        else:
            genre_count[genre] = 1
    print("Genre Counts:", genre_count)
     


def newestAndOldestMovies(movies):
    newest = movies[0]
    oldest = movies[0]
    for movie in movies:
        if movie["year"] > newest["year"]:
            newest = movie
        if movie["year"] < oldest["year"]:
            oldest = movie
    print("Newest:", newest["name"], "(", newest["year"], "),", "Oldest:", oldest["name"], "(", oldest["year"], ")")
     


def moviesByGenre(movies, genre):
    filtered_movies = []
    for movie in movies:
        if movie["genre"].lower() == genre.lower():
            filtered_movies.append(movie["name"])
    if filtered_movies:
        movie_list = ", ".join(filtered_movies)
    else:
        movie_list = "None found"
    print("Movies in genre '" + genre + "':", movie_list)
     


def moviesByYear(movies, year):
    filtered_movies = []
    for movie in movies:
        if movie["year"] == year:
            filtered_movies.append(movie["name"])
    if filtered_movies:
        movie_list = ", ".join(filtered_movies)
    else:
        movie_list = "None found"
    print("Movies released in", year, ":", movie_list)
    


def countMoviesByDirector(movies):
    director_count = {}
    for movie in movies:
        director = movie["director"]
        if director in director_count:
            director_count[director] += 1
        else:
            director_count[director] = 1
    print("Movies by Director:", director_count)
     


 
def main():
    functions = {
        "1": ("Print first n movies", firstNMovies),
        "2": ("Get total number of movies", totalMovies),
        "3": ("Get highest-rated movie", highestRatedMovie),
        "4": ("Calculate average rating", averageRating),
        "5": ("Get movies before 2000", pre200Movies),
        "6": ("Get movies above rating 8.0", highRatedMovies),
        "7": ("Get genre count", genreCount),
        "8": ("Get newest and oldest movies", newestAndOldestMovies),
        "9": ("Filter movies by genre", moviesByGenre),
        "10": ("Filter movies by year", moviesByYear),
        "11": ("Count movies by director", countMoviesByDirector),
    }
    
    while True:
        print("\nAvailable functions:")
        for k, v in functions.items():
            print(f"{k}: {v[0]}")
        choice = input("Choose a function or 'q' to quit: ")
        if choice.lower() == 'q':
            break
        if choice in functions:
            if choice == "1":
                functions[choice][1](movies, int(input("Enter number: ")))
            elif choice == "6":
                functions[choice][1](movies, float(input("Enter min (default 8.0): ") or 8.0))
            elif choice == "9":
                functions[choice][1](movies, input("Enter genre: "))
            elif choice == "10":
                functions[choice][1](movies, int(input("Enter year: ")))
            else:
                functions[choice][1](movies)
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
