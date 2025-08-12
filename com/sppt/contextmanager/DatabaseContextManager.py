import sqlite3
from typing import List, Dict, Union


class SQLiteConnection:
    """Custom context manager for SQLite3 Database"""

    def __init__(self, db_name: str) -> None:
        print(f'Inside SQLite3Connection __init__ method')
        self.db_name = db_name
        self.connection = None

    def __enter__(self) -> sqlite3.Connection:
        print(f'Inside SQLite3Connection __enter__ method')
        self.connection = sqlite3.connect(self.db_name)
        return self.connection

    def __exit__(self, exc_type, exc_value, traceback) -> None:
        print(f'Inside SQLite3Connection __exit__ method')
        if self.connection:
            if exc_type is None:  # No exceptions, commit changes
                self.connection.commit()
            self.connection.close()


Book = Dict[str, Union[str, int]]


class BookReader:
    def createTable(self) -> None:
        with SQLiteConnection('my_database.db') as conn:
            sqlquery = "CREATE TABLE IF NOT EXISTS Books(name text primary key,author text,read integer)"
            cursor = conn.cursor()
            cursor.execute(sqlquery)

    def delete_book(self, book_name):
        with SQLiteConnection('my_database.db') as conn:
            sqlquery = "DELETE FROM Books WHERE name = ?"
            cursor = conn.cursor()
            cursor.execute(sqlquery, (book_name,))

    def add_book(self, name: str, author: str) -> None:
        with SQLiteConnection('my_database.db') as conn:
            sqlquery = "INSERT INTO Books(name,author,read) values(?,?,?)"
            cursor = conn.cursor()
            cursor.execute(sqlquery, (name, author, 0))

    def get_all_books(self) -> List[Book]:
        with SQLiteConnection('my_database.db') as conn:
            cursor = conn.cursor()
            sqlquery = "SELECT * from Books"
            cursor.execute(sqlquery)
            rows = cursor.fetchall()
            print(f'Result Size:{len(rows)}')

            return [
                {"name": row[0], "author": row[1], "read": row[2]}
                for row in rows
            ]


if __name__ == "__main__":
    bookreader = BookReader()
    bookreader.createTable()

    bookreader.delete_book("The law of Zaro")
    bookreader.delete_book("The Zaro civilization")

    bookreader.add_book("The law of Zaro", "Dexter")
    bookreader.add_book("The Zaro civilization", "Alex K")

    books = bookreader.get_all_books()
    for book in books:
        print(f" \"name\":{book['name']},\"author\": {book['author']}, \"read\": {book['read']}")
