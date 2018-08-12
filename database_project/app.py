from utils import database

USER_CHOICE = """
- 'a': add
- 'l': list
- 'r': mark as read
- 'd': delete a book
- 'q': quit
"""

def menu():
    try:
        database.books = database.read_from_file('books.txt')
        database.reload_indexes()
    except FileNotFoundError:
        pass

    while True:
        user_input = input(f'{USER_CHOICE} \nWhat is your choice?')
        if user_input == 'a':
            database.add_book()
            database.book_index += 1
            database.save_to_file('books.txt', database.books)
        elif user_input == 'l':
            database.list_books()
        elif user_input == 'r':
            database.mark_as_read()
            database.save_to_file('books.txt', database.books)
        elif user_input == 'd':
            database.delete_book()
            database.save_to_file('books.txt', database.books)
        elif user_input == 'q':
            print('Goodbye')
            break
        else:
            print('Invalid option')

menu()