import sqlite3


def create_tables(conn):
    conn.execute("""
    CREATE TABLE IF NOT EXISTS books (
        id INTEGER PRIMARY KEY,
        name TEXT,
        author TEXT,
        publication_year INTEGER,
        genre TEXT,
        number_of_pages INTEGER,
        number_of_copies INTEGER
        
)
""")


def insert_books(
    conn, name, author, publication_year, genre, number_of_pages, number_of_copies
):
    conn.execute(
        """
    INSERT INTO books (name, author, publication_year, genre, number_of_pages, number_of_copies)
    VALUES (?, ?, ?, ?, ?, ?)
    """,
        (name, author, publication_year, genre, number_of_pages, number_of_copies),
    )
    conn.commit()


if __name__ == "__main__":
    connect = sqlite3.connect("database.sqlite")
    create_tables(connect)
    insert_books(connect, "Война и мир", "Лев Толстой", 1869, "Роман", 1225, 5)
    insert_books(connect, "Преступление и наказание", "Фёдор Достоевский", 1866, "Роман", 672, 4)

    connect.close()
