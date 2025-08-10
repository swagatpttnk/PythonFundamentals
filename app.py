MENU_PROMPT = "\nEnter 'a' to add a movie, 'l' to see your movies, 'f' to find a movie by title, or 'q' to quit: "
movies = []


def add_movie():
    title = input("Enter the movie title:")
    director = input("Enter the movie director name:")
    year = input("Enter the movie release year:")
    movies.append({
        'title': title,
        'director': director,
        'year': year
    })


def print_movie(movie):
    print(f"Title:{movie['title']}")
    print(f"Director: {movie['director']}")
    print(f"Release year: {movie['year']}")


def list_movies():
    for movie in movies:
        print_movie(movie)


def find_movie():
    search_title = input("Enter the movie title you are looking for:")
    for movie in movies:
        if movie['title'] == search_title:
            print_movie(movie)

"""
selection = input(MENU_PROMPT)
while selection != 'q':
    if selection == "a":
        add_movie()
    elif selection == "l":
        list_movies()
    elif selection == "f":
        find_movie()
    else:
        print('Unknown command. Please try again.')

    selection = input(MENU_PROMPT)
"""


user_options={
    'a': add_movie,
    'l': list_movies,
    'f': find_movie
}
def menu():
    selection = input(MENU_PROMPT)
    while selection != 'q':
        if selection in user_options:
            selected_function = user_options[selection]
            selected_function()
        else:
            print('unknown command please try again.')

        selection = input(MENU_PROMPT)


menu()