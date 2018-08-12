movies = []

"""
movie = {
    'name': ... (str)
    'director': ...(str)    
    'year': ... (int)
"""


def menu():
    user_input = input("Choose an option:")
    while user_input != 'q':
        if user_input == 'a':
            add_movie()
        elif user_input == 's':
            show_movies(movies)
        elif user_input == 'f':
            find_movies()
        else:
            print('Unknown command...')

        user_input = input("\nChoose an option:")


def add_movie():
    name = input('Enter name:')
    director = input('Enter director:')
    year = input('Year')

    movies.append({
        'name': name,
        'director': director,
        'year': year
    })


def show_movies(movies_list):
    for movie in movies_list:
        show_movie_details(movie)


def show_movie_details(movie):
    print(f"Name: {movie['name']}")
    print(f"Director: {movie['director']}")
    print(f"Year: {movie['year']}")


def find_movies():
    property = input('What property?')
    looking_for = input('What are you looking for?')

    found_movies = find_by_attrib(looking_for, lambda x: x[property])

    show_movies(found_movies)


def find_by_attrib(expected, finder):
    found = []

    for movie in movies:
        if finder(movie) == expected:
            found.append(movie)

    return found


menu()

print(movies)
