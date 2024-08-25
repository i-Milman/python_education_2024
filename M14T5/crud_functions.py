import sqlite3


def sql_connection(func):
    def wrapper(*args, **kwargs):
        conn: sqlite3.connect = sqlite3.connect('data.db')
        try:
            cursor: sqlite3.Cursor = conn.cursor()
            return func(cursor, *args, **kwargs)  # Передаем cursor в функцию
        finally:
            conn.commit()
            conn.close()
    return wrapper


@sql_connection
def initiate_db(cursor: sqlite3.Cursor) -> None:
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Products
    (
        id INTEGER PRIMARY KEY,
        title TEXT NOT NULL,
        description TEXT,
        price INTEGER NOT NULL
    )
    """)
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Users
    (
        id INTEGER PRIMARY KEY,
        username TEXT NOT NULL,
        email TEXT NOT NULL,
        age INTEGER NOT NULL,
        balance INTEGER NOT NULL
    )
    """)


@sql_connection
def get_all_products(cursor: sqlite3.Cursor) -> list:
    cursor.execute("""
    SELECT *
    FROM Products
    """)
    result = cursor.fetchall()
    return result if len(result) else None


@sql_connection
def add_product(cursor: sqlite3.Cursor, title: str, description: str, price: int) -> None:
    cursor.execute("""
    INSERT INTO Products
    (title, description, price)
    VALUES (?, ?, ?)
    """, (title, description, price))


@sql_connection
def add_user(cursor: sqlite3.Cursor, username: str, email: str, age: int) -> None:
    cursor.execute("""
    INSERT INTO Users
    (username, email, age, balance)
    VALUES (?, ?, ?, ?)
    """, (username, email, age, 1000))


@sql_connection
def is_included(cursor: sqlite3.Cursor, username) -> bool:
    cursor.execute("""
        SELECT *
        FROM Users
        WHERE username = ?
        """, (username,))
    result = cursor.fetchall()
    return True if len(result) else False


# initiate_db()
# [add_product(f'Продукт {i}', f'Описание {i}', i * 100) for i in range(1,5)]

