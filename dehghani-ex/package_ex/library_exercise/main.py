from library import *

lib = Library()
lib.add_book('Ditel and Ditel ', 'Ditel')
lib.show_books()

def user_cmd_input(user_cmd_i : str):
    user_cmd_l = user_cmd_i.lower()
    if user_cmd_l == 'add' or user_cmd_l == '1':
        return 'add'
    elif user_cmd_l == 'remove' or user_cmd_l == '2':
        return 'remove'
    elif user_cmd_l == 'search' or user_cmd_l == '3':
        return 'search'
    else:
        return 'exit'

def proceed_cmd(cmd_user_f: str):
    if cmd_user_f == 'add':
       adding_book_from_usr()
    if cmd_user_f == 'remove':
        book_name_to_del = input('Enter book name to delete: ')
        lib.remove_book(book_name_to_del)
    if cmd_user_f == 'search':
        user_search_book()


def user_search_book():
    book_name_to_search = input('Enter book name to search: ')
    result_search_book = lib.search_book(book_name_to_search)
    print(result_search_book) if result_search_book is not None else print('no book found!')


def adding_book_from_usr():
    book_name = input("send book title: ")
    book_author = input("send book author: ")
    lib.add_book(book_name, book_author)


def begin_to_explore():
    print("\n\tWelcome to MELI library!")
    user_cmd_f = 'show_main_menu'
    while user_cmd_f != 'exit':
        print("""
        Choose command:
            1- adding book (1 or add)
            2- remove book (2 or remove)
            3- search books (3 or search)
            4- exit
        """)
        user_cmd_f = user_cmd_input(input())
        print(f"your command is = {user_cmd_f}")
        proceed_cmd(user_cmd_f)


if __name__ == '__main__':
    begin_to_explore()
