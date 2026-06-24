print("Library Management System")
import sqlite3

DB_NAME = "library.db"

def connect():
    return sqlite3.connect(DB_NAME)

def create_table():
    conn = connect()
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS books (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            author TEXT NOT NULL,
            year INTEGER NOT NULL,
            available INTEGER DEFAULT 1
        )
    """)
    conn.commit()
    conn.close()

def add_book():
    title = input("Book title: ")
    author = input("Author: ")
    year = int(input("Year: "))

    conn = connect()
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO books (title, author, year, available) VALUES (?, ?, ?, ?)",
        (title, author, year, 1)
    )
    conn.commit()
    conn.close()
    print("Book added successfully.")

def view_books():
    conn = connect()
    cur = conn.cursor()
    cur.execute("SELECT * FROM books")
    books = cur.fetchall()
    conn.close()

    if not books:
        print("No books found.")
    else:
        for book in books:
            status = "Available" if book[4] == 1 else "Borrowed"
            print(f"ID: {book[0]} | Title: {book[1]} | Author: {book[2]} | Year: {book[3]} | Status: {status}")

def borrow_book():
    book_id = int(input("Enter book ID to borrow: "))

    conn = connect()
    cur = conn.cursor()
    cur.execute("UPDATE books SET available = 0 WHERE id = ?", (book_id,))
    conn.commit()
    conn.close()
    print("Book borrowed successfully.")

def return_book():
    book_id = int(input("Enter book ID to return: "))

    conn = connect()
    cur = conn.cursor()
    cur.execute("UPDATE books SET available = 1 WHERE id = ?", (book_id,))
    conn.commit()
    conn.close()
    print("Book returned successfully.")

def delete_book():
    book_id = int(input("Enter book ID to delete: "))

    conn = connect()
    cur = conn.cursor()
    cur.execute("DELETE FROM books WHERE id = ?", (book_id,))
    conn.commit()
    conn.close()
    print("Book deleted successfully.")

def menu():
    create_table()

    while True:
        print("\nLibrary Management System")
        print("1. Add Book")
        print("2. View Books")
        print("3. Borrow Book")
        print("4. Return Book")
        print("5. Delete Book")
        print("6. Exit")

        choice = input("Choose option: ")

        if choice == "1":
            add_book()
        elif choice == "2":
            view_books()
        elif choice == "3":
            borrow_book()
        elif choice == "4":
            return_book()
        elif choice == "5":
            delete_book()
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid choice.")

menu()
