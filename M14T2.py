# Задача "Средний баланс пользователя":
# Для решения этой задачи вам понадобится решение предыдущей.
# Для решения необходимо дополнить существующий код:
# Удалите из базы данных not_telegram.db запись с id = 6.
# Подсчитать общее количество записей.
# Посчитать сумму всех балансов.
# Вывести в консоль средний баланс всех пользователя.

# Решение:
from sqlite3 import connect

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

# Удаление пользователя с id=6
cursor.execute("""
DELETE
FROM Users
WHERE id = ?
""", (6,))

# Подсчёт кол-ва всех пользователей
cursor.execute("""
SELECT COUNT(*)
FROM Users
""")
total_users = cursor.fetchone()[0]

# Подсчёт суммы всех балансов
cursor.execute("""
SELECT SUM(balance)
FROM Users
""")
total_balances = cursor.fetchone()[0]

print(f'Cредний баланс всех пользователей: {total_balances/total_users}')

# Запись результата
conn.commit()
# Завершение работы с БД
conn.close()







