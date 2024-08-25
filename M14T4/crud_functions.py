from sqlite3 import connect


def sql_connection(func):
    def wrapper(*args, **kwargs):
        conn = connect('data.db')
        try:
            cursor = conn.cursor()
            return func(cursor, *args, **kwargs)  # Передаем cursor в функцию
        finally:
            conn.commit()
            conn.close()
    return wrapper


@sql_connection
def initiate_db(cursor) -> None:
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Products
    (
        id INTEGER PRIMARY KEY,
        title TEXT NOT NULL,
        description TEXT,
        price INTEGER NOT NULL
    )
    """)


@sql_connection
def get_all_products(cursor):
    cursor.execute("""
    SELECT *
    FROM Products
    """)
    result = cursor.fetchall()
    return result if result is not None else 0


@sql_connection
def add_product(cursor, title, description, price):
    cursor.execute("""
    INSERT INTO Products
    (title, description, price)
    VALUES (?, ?, ?)
    """, (title, description, price))


# initiate_db()
# [add_product(f'Продукт {i}', f'Описание {i}', i * 100) for i in range(1,5)]
print(get_all_products())
