from utils import database

USER_CHOICE = """
- 'a': add
- 'l': list
- 'r': mark as read
- 'd': delete a book
- 'q': quit
"""


def menu():

    database.create_book_table()

    while True:
        user_input = input(f'{USER_CHOICE} \nWhat is your choice?')
        if user_input == 'a':
            database.add_book()
        elif user_input == 'l':
            database.list_books()
        elif user_input == 'r':
            database.mark_as_read()
        elif user_input == 'd':
            database.delete_book()
        elif user_input == 'q':
            print('Goodbye')
            break
        else:
            print('Invalid option')


menu()
