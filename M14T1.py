# Задача "Первые пользователи":
# Создайте файл базы данных not_telegram.db и подключитесь к ней, используя встроенную библиотеку sqlite3.
# Создайте объект курсора и выполните следующие действия при помощи SQL запросов:
# Создайте таблицу Users, если она ещё не создана. В этой таблице должны присутствовать следующие поля:
# id - целое число, первичный ключ
# username - текст (не пустой)
# email - текст (не пустой)
# age - целое число
# balance - целое число (не пустой)
# Заполните её 10 записями:
# User1, example1@gmail.com, 10, 1000
# User2, example2@gmail.com, 20, 1000
# User3, example3@gmail.com, 30, 1000
# ...
# User10, example10@gmail.com, 100, 1000
# Обновите balance у каждой 2ой записи начиная с 1ой на 500:
# User1, example1@gmail.com, 10, 500
# User2, example2@gmail.com, 20, 1000
# User3, example3@gmail.com, 30, 500
# ...
# User10, example10@gmail.com, 100, 1000
# Удалите каждую 3ую запись в таблице начиная с 1ой:
# User2, example2@gmail.com, 20, 1000
# User3, example3@gmail.com, 30, 500
# User5, example5@gmail.com, 50, 500
# ...
# User9, example9@gmail.com, 90, 500
#
# Сделайте выборку всех записей при помощи fetchall(), где возраст не равен 60
# и выведите их в консоль в следующем формате (без id):
# Имя: <username> | Почта: <email> | Возраст: <age> | Баланс: <balance>

# Решение:
from sqlite3 import connect
import pandas as pd

# Настройка соединения с БД
conn = connect("not_telegram.db")
cursor = conn.cursor()

# Создание таблицы
cursor.execute("""
CREATE TABLE IF NOT EXISTS Users
(
    id INTEGER PRIMARY KEY,
    username TEXT NOT NULL,
    email TEXT NOT NULL,
    age INTEGER,
    balance INT NOT NULL
)
""")

# Заполнение таблицы
for n in range(1, 11):
    cursor.execute("""
    INSERT INTO Users 
    (username, email, age, balance)
    VALUES (?, ?, ?, ?)
    """, (f'User{n}', f'example{n}@gmail.com', f'{n}0', '1000'))

# Обновление таблицы
for n in range(1, 11):
    if not (n-1) % 2:
        cursor.execute("""
        UPDATE Users
        SET balance = 500
        WHERE id = ?
        """, (n,))

# Удаление элементов
for n in range(1, 11):
    if not (n-1) % 3:
        cursor.execute("""
        DELETE
        FROM Users
        WHERE id = ?
        """, (n,))

# Вывод в терминал
cursor.execute("""
SELECT username, email, age, balance
FROM Users
WHERE age != 60
""")
[print(f'Имя: {username} | Почта: {email} | Возраст: {age} | Баланс: {balance}')
 for username, email, age, balance in cursor.fetchall()]
print()

# Вывод в терминал c помощью pandas
df = pd.read_sql("""
SELECT *
FROM Users
WHERE age != 60
""", conn, index_col='id')
df.rename(columns={'username':'Имя', 'email':'Почта', 'age':'Возраст', 'balance':'Баланс'}, inplace=True)
print(df)

# Запись результата
conn.commit()
# Завершение работы с БД
conn.close()







