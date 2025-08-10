from com.sppt.database.utils import database
from com.sppt.database.utils.database import DAO


class DatabaseDemo:
    DB_MODE = """
    ENTER THE DB MODE FOR THIS PROG:
    - 'l' - for list mode
    - 'f' - for File Mode
    - 's' - for SQLite Mode
    Your Choice:
    """
    USER_CHOICE = """
    ENTER :
    - 'a' - to add new books
    - 'l' - to list all books
    - 'r' - to mark the book as read
    - 'd' - to delete a book
    - 'q' - to quit
    Your Choice:
    """

    def __init__(self):
        self.dbmanager = None
        self.availabledbmodes = ['l', 'f', 's']
        self.availableappmodes = ['l', 'a', 'r', 'd']

    def getDBMode(self):
        inputmode = input(self.DB_MODE)
        while inputmode not in self.availabledbmodes:
            print(f'invalid input:{inputmode} \n')
            inputmode = input(self.DB_MODE)
        return DAO(inputmode)

    def menu(self):
        self.dbmanager = self.getDBMode()

        user_input = input(self.USER_CHOICE)
        while user_input != 'q':
            if user_input == 'a':
                self.prompt_add_book()
            elif user_input == 'l':
                self.list_books()
            elif user_input == 'r':
                self.mark_book_as_read()
            elif user_input == 'd':
                self.prompt_delete_book()
            else:
                print("Unknown command , Please try again:")
            user_input = input(self.USER_CHOICE)

    def prompt_add_book(self):
        name = input("Enter the new book name:")
        author = input("Enter the new book author name:")
        self.dbmanager.add_book(name, author)

    def list_books(self):
        books = self.dbmanager.get_all_books()
        for book in books:
            print(f" book['read']:{book['read']}")
            read = 'YES' if str(book['read']) == '1' else 'NO'
            print(f"{book['name']} by {book['author']},read: {read}")

    def mark_book_as_read(self):
        book_name = input('Enter the book name to be marked as read:')
        self.dbmanager.mark_book_as_read(book_name)

    def prompt_delete_book(self):
        book_name = input('Enter the book name to be deleted:')
        self.dbmanager.delete_book(book_name)
