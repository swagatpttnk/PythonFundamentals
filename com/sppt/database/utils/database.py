import sqlite3


class DAO:
    def __init__(self, dbmode):
        self.dbmode = dbmode  # add check if anything else is added
        self.init_mode()

    def add_book_listmode(self, name, author):
        self.books.append({'name': name, 'author': author, 'read': 0})
        print(f"After Addition, self.books.size:{len(self.books)}")

    def get_all_books_listmode(self):
        print(f"inside get_all_books:{self.dbmode} , self.books.size: {len(self.books)}")
        return self.books

    def mark_book_as_read_listmode(self, book_name):
        for book in self.books:
            if book['name'] == book_name:
                book['read'] = 1

    def delete_book_listmode(self, bookname):
        self.books = [book for book in self.books if book['name'] != bookname]

    # -------
    def init_filetmode(self):
        with open(self.books_file, 'a') as file:
            pass

    def add_book_filemode(self, name, author):
        with open(self.books_file, 'a') as file:
            file.write(f"{name},{author},0\n")

    def get_all_books_filemode(self):
        with open(self.books_file, 'r') as file:
            lines = [line.strip() for line in file.readlines()]
            print(f"Lines:{lines}")
            return [
                {'name': line.split(',')[0], 'author': line.split(',')[1], 'read': line.split(',')[2]}
                for line in lines
            ]

    def mark_book_as_read_filemode(self, book_name):
        all_books = self.get_all_books_filemode()
        for book in all_books:
            if book['name'] == book_name:
                book['read'] = '1'
        self._save_all_books(all_books)

    def _save_all_books(self, all_books):
        with open(self.books_file, 'w') as file:
            for book in all_books:
                file.write(f"{book['name']},{book['author']},{book['read']}\n")

    def delete_book_filemode(self, bookname):
        all_books = self.get_all_books_filemode()
        all_books = [book for book in all_books if book['name'] != bookname]
        self._save_all_books(all_books)

    # ---- generic function ----
    def mark_book_as_read(self, book_name):
        if self.dbmode == 'l':
            self.mark_book_as_read_listmode(book_name)
        elif self.dbmode == 'f':
            self.mark_book_as_read_filemode(book_name)
        elif self.dbmode == 's':
            self.mark_book_as_read_sqlmode(book_name)

    def add_book(self, name, author):
        if self.dbmode == 'l':
            self.add_book_listmode(name, author)
        elif self.dbmode == 'f':
            self.add_book_filemode(name, author)
        elif self.dbmode == 's':
            self.add_book_sqlmode(name, author)

    #    self.add_book_sqlmode(book_name)
    def delete_book(self, book_name):
        if self.dbmode == 'l':
            self.delete_book_listmode(book_name)
        elif self.dbmode == 'f':
            self.delete_book_filemode(book_name)
        elif self.dbmode == 's':
            self.delete_book_sqlmode(book_name)

    def get_all_books(self):
        print(f"inside get_all_books:{self.dbmode}")
        if self.dbmode == 'l':
            return self.get_all_books_listmode()
        elif self.dbmode == 'f':
            return self.get_all_books_filemode()
        elif self.dbmode == 's':
            return self.get_all_books_sqlmode()

    def init_mode(self):
        print(f"initialized DAO with dbmode:{self.dbmode}")
        if self.dbmode == 'l':
            self.books = []
            print(f"initialized DAO with  self.books.size:{len(self.books)}")
        elif self.dbmode == 'f':
            self.books_file = 'books.txt'
            self.init_filetmode()
        elif self.dbmode == 's':
            sqlquery = "CREATE TABLE IF NOT EXISTS Books(name text primary key,author text,read integer)"
            connection = sqlite3.connect('my_database.db')
            cursor = connection.cursor()
            cursor.execute(sqlquery)
            connection.commit()
            connection.close()

    def add_book_sqlmode(self, name, author):
        sqlquery = "INSERT INTO Books(name,author,read) values(?,?,?)"
        connection = sqlite3.connect('my_database.db')
        cursor = connection.cursor()
        cursor.execute(sqlquery, (name, author, 0))
        connection.commit()
        connection.close()

    def get_all_books_sqlmode(self):
        sqlquery = "SELECT * from Books"
        connection = sqlite3.connect('my_database.db')
        cursor = connection.cursor()
        cursor.execute(sqlquery)
        rows = cursor.fetchall()
        print(f'Result Size:{len(rows)}')
        connection.close()
        return [
            {"name": row[0], "author": row[1], "read": row[2] }
            for row in rows
        ]

    def mark_book_as_read_sqlmode(self, book_name):
        sqlquery = "UPDATE Books set read=? WHERE name=?"
        connection = sqlite3.connect('my_database.db')
        cursor = connection.cursor()
        cursor.execute(sqlquery, (1, book_name))
        connection.commit()
        connection.close()

    def delete_book_sqlmode(self, book_name):
        sqlquery = "DELETE FROM Books WHERE name=?"
        connection = sqlite3.connect('my_database.db')
        cursor = connection.cursor()
        cursor.execute(sqlquery, (book_name))
        connection.commit()
        connection.close()
