movies = [{'name': 'Matrix', 'director': 'Cichy', 'year': '1999'},
          {'name': 'Star wars', 'director': 'Wachowski', 'year': '1999'}]

for movie in movies:
    print(movie.values())
    print(list(movie.keys()))
    print(list(movie.items()))


def main_menu():
    while True:

        print("Welcome user. Choose an action:")
        print("A - add a movie")
        print("V - view your movies")
        print("F - find a movie")
        print("Q - quit a program")

        action = input("Your decision:")

        if action.lower() not in ['a', 'v', 'f', 'q']:
            print('Unrecognizable option selected! Try again.' + '\n')

        if action.lower() == 'a':
            new_movie = {}
            movie_name = input('Enter movie name:')
            movie_director = input('Enter movie director:')
            movie_year = input('Enter movie year of making:')
            new_movie['name'] = movie_name
            new_movie['director'] = movie_director
            new_movie['year'] = movie_year

            movies.append(new_movie)
            print('Movie added!')

        if action.lower() == 'v':
            for movie in movies:
                print('\n')
                print('name: ' + movie['name'])
                print('director: ' + movie['director'])
                print('year: ' + movie['year'] + '\n')

        if action.lower() == 'f':
            attribute = input('By what attribute would you like to find a movie? (name, director, year)?')

            if attribute not in ['name', 'director', 'year']:
                print('Unrecognized attribute! Try again')

            if attribute == 'name':
                name_att = input('Enter movie name:')
                for movie in movies:
                    if name_att in movie.values():
                        print('Movie found!')
                        print('\n')
                        print('name: ' + movie['name'])
                        print('director: ' + movie['director'])
                        print('year: ' + movie['year'] + '\n')
                        # break

                    else:
                        continue
                else:
                    print('Movie not found!')

            if attribute == 'director':
                name_att = input('Enter movie director:')
                for movie in movies:
                    if name_att in movie.values():
                        print('Movie found! by director!')
                        print('name: ' + movie['name'])
                        print('director: ' + movie['director'])
                        print('year: ' + movie['year'] + '\n')
                        # break

                    else:
                        continue
                else:
                    print('Movie not found!')

            if attribute == 'year':
                name_att = input('Enter movie year:')
                for movie in movies:
                    if name_att in movie.values():
                        print('Movie found!')
                        print('name: ' + movie['name'])
                        print('director: ' + movie['director'])
                        print('year: ' + movie['year'] + '\n')
                        # break

                    else:
                        continue
                else:
                    print('Movie not found!')

        if action.lower() == 'q':
            break


main_menu()
