import os

# File path for movie records
file_path = "E:/cap776CA1/CA2/movie.csv"

# Ensure the file exists or create an empty file if not
def ensure_file():
    if not os.path.exists(file_path):
        with open(file_path, 'w') as file:
            file.write('Name,Year,Genre\n')

# Helper function to read all movies into a list of dictionaries
def read_movies():
    movies = []
    with open(file_path, 'r') as file:
        lines = file.readlines()[1:]  # Skip the header
        for line in lines:
            line = line.strip()
            values = line.split(',')
            if len(values) == 3:
                name, year, genre = values
                movies.append({'Name': name, 'Year': year, 'Genre': genre})
            
    return movies


# Helper function to write movies back to the CSV file
def write_movies(movies):
    with open(file_path, 'w') as file:
        file.write('Name,Year,Genre\n')
        for movie in movies:
            file.write(f"{movie['Name']},{movie['Year']},{movie['Genre']}\n")

# 1. Function to add a new movie
def add_movie():
    ensure_file()  # Ensure file exists
    name = input("Enter the movie name: ")
    year = input("Enter the movie year: ")
    genre = input("Enter the movie genre: ")

    movies = read_movies()  # Read current records
    movies.append({'Name': name, 'Year': year, 'Genre': genre})
    write_movies(movies)  # Save the new movie

    print(f"Movie '{name}' added successfully!")

# 2. Function to view all movies
def view_movies():
    ensure_file()
    movies = read_movies()

    if movies:
        print("\n--- Movie Records ---")
        for movie in movies:
            print(f"{movie['Name']} | {movie['Year']} | {movie['Genre']}")
        print("------------------------\n")
    else:
        print("No movie records available.\n")

# 3. Function to update a movie record
def update_movie():
    ensure_file()
    name_to_update = input("Enter the name of the movie to update: ")

    movies = read_movies()
    for movie in movies:
        if movie['Name'] == name_to_update:
            new_year = input("Enter new year: ")
            new_genre = input("Enter new genre: ")
            movie['Year'] = new_year
            movie['Genre'] = new_genre
            write_movies(movies)
            print(f"Record for '{name_to_update}' updated successfully!")
            return

    print(f"Movie '{name_to_update}' not found.")

# 4. Function to delete a movie record
def delete_movie():
    ensure_file()
    name_to_delete = input("Enter the name of the movie to delete: ")

    movies = read_movies()
    for movie in movies:
        if movie['Name'] == name_to_delete:
            movies.remove(movie)
            write_movies(movies)
            print(f"Record for '{name_to_delete}' deleted successfully!")
            return

    print(f"Movie '{name_to_delete}' not found.")

# Menu system to interact with the system
def menu():
    while True:
        print("\n   Movie Management System ")
        print("1. Add Movie")
        print("2. View Movies")
        print("3. Update Movie")
        print("4. Delete Movie")
        print("5. Exit")
        
        choice = input("Esme se kuch choose kro (1-5): ")

        if choice == '1':
            add_movie()
        elif choice == '2':
            view_movies()
        elif choice == '3':
            update_movie()
        elif choice == '4':
            delete_movie()
        elif choice == '5':
            print("Bye Bye have a nice day!")
            break
        else:
            print("Shi option choose kro yaar.")
# to ensure that the file exists or not otherwise this function will create a new file to that location 
ensure_file()
# this function will work as a menu grid to the user and print the available functions
menu()
