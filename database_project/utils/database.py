# books = [{
#     'name': 'Matrix',
#     'author': 'Jeremy Irons',
#     'read': False,
#     'book_index': 1
# },
#     {
#         'name': '1984',
#         'author': 'Orwell',
#         'read': False,
#         'book_index': 2
#     },
#     {
#         'name': 'Brand New World',
#         'author': 'Huxley',
#         'read': False,
#         'book_index': 3
#     }
# ]

books = []

book_index = len(books) + 1


def add_book():
    global book_index
    book = input('Enter a book name: ')
    author = input('Enter a book author: ')
    data = {
        'name': book,
        'author': author,
        'read': False,
        'book_index': book_index
    }
    books.append(data)
    print('Book added!')


def list_books():
    print('Your current collection: ')
    if books:
        for book in books:
            print(
                f"{book['book_index']}. Book name: {book['name']}, author: {book['author']}, status: {'Read' if book['read'] == True else 'Not read'}.")
    else:
        print('No books yet!')


def mark_as_read():
    list_books()
    print('\n')
    book_inner = input('Select a book to mark as read: ')
    book_inner = book_index_verifier(book_inner)
    for book in books:
        if book['book_index'] == int(book_inner):
            if book['read'] == True:
                print('Book already marked.')
                return
            else:
                book['read'] = True
                print('Book marked as read.')
                return
    else:
        print('No such book index.')


def delete_book():
    list_books()
    print('\n')
    book_inner = input('Mark a book to delete: ')
    book_inner = book_index_verifier(book_inner)
    for book in books:
        if book['book_index'] == int(book_inner):
            del books[books.index(book)]
            print('Book deleted.')
            reload_indexes()
            return
    else:
        print('No such book index.')


def book_index_verifier(index_input):
    try:
        if int(index_input) <= 0 or int(index_input) > len(books):
            return 0
        return index_input
    except ValueError:
        print('Enter a number please.')
        return 0


def reload_indexes():
    global book_index
    book_index = 1
    for book in books:
        book['book_index'] = book_index
        book_index += 1


def save_to_file(filename, content):
    with open(filename, 'w') as file:
        for line in content:
            name, author, read, index = line['name'], line['author'], line['read'], line['book_index']
            file.writelines(f'{name}, {author}, {read}, {index}\n')


def read_from_file(filename):
    with open(filename, 'r') as file:
        temporary_list = []
        file = file.readlines()
        file = [line.strip() for line in file]
        for line in file:
            line = line.split(', ')
            data = {
                'name': line[0],
                'author': line[1],
                'read': line[2],
                'book_index': int(line[3])
            }
            temporary_list.append(data)
        return temporary_list
