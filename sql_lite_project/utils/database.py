import sqlite3


def add_book():
    book_index = _set_book_index() + 1
    book = input('Enter a book name: ')
    author = input('Enter a book author: ')
    connection = sqlite3.connect('data.db')
    cursor = connection.cursor()

    cursor.execute('INSERT INTO books VALUES(?, ?, ?, 0)',
                   (book_index, book, author))

    connection.commit()
    connection.close()


def list_books():
    if _get_books_from_database():
        print('Your current collection: ')
        books = _get_books_from_database()
        for row in books:
            print(
                f"{row[0]}. Book name: {row[1]}, author: {row[2]}, status: {'Read' if row[3] == 1 else 'Not read'}.")
    else:
        print('No books yet!')


def _set_book_index():
    connection = sqlite3.connect('data.db')
    cursor = connection.cursor()

    cursor.execute('SELECT count(*) FROM books')
    result = cursor.fetchall()

    connection.commit()
    connection.close()
    return result[0][0]





def _update_book_item(column, item, value):
    connection = sqlite3.connect('data.db')
    cursor = connection.cursor()

    cursor.execute(f'UPDATE books SET {column} = {value} where id = {item}')

    connection.commit()
    connection.close()


def _delete_book_item(value):
    connection = sqlite3.connect('data.db')
    cursor = connection.cursor()

    cursor.execute(f'DELETE from books where id = {value}')

    connection.commit()
    connection.close()


def _get_books_from_database():
    connection = sqlite3.connect('data.db')
    cursor = connection.cursor()

    cursor.execute('SELECT * FROM books')
    result = cursor.fetchall()

    connection.commit()
    connection.close()
    return result


def mark_as_read():
    list_books()
    print('\n')
    book_inner = input('Select a book to mark as read: ')
    book_inner = _book_index_verifier(book_inner)
    if book_inner:
        books = _get_books_from_database()
        for row in books:
            if row[0] == int(book_inner):
                if row[3] == 1:
                    print('Book already marked.')
                else:
                    _update_book_item('read', row[0], 1)
                    print('Book marked as read.')


def delete_book():
    list_books()
    print('\n')
    book_inner = input('Mark a book to delete: ')
    book_inner = _book_index_verifier(book_inner)
    if book_inner:
        books = _get_books_from_database()
        for row in books:
            if row[0] == int(book_inner):
                _delete_book_item(row[0])
                print('Book deleted.')
    _reload_indexes()


def _book_index_verifier(index_input):
    book_index = _set_book_index() + 1
    try:
        if int(index_input) <= 0 or int(index_input) > book_index:
            print('No such book index.')
            return 0
        return index_input
    except ValueError:
        print('Enter a number please.')
        return 0


def _reload_indexes():
    books = _get_books_from_database()
    i = 1
    for row in books:
        _update_book_item('id', row[0], i)
        i += 1
    return i


def create_book_table():
    connection = sqlite3.connect('data.db')
    cursor = connection.cursor()

    cursor.execute(
        'CREATE TABLE books(id integer primary key, name text, author text, read integer)')

    connection.commit()
    connection.close()
