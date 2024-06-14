# Задача:
# Реализуйте программу, которая имитирует доступ к общему ресурсу с использованием механизма блокировки потоков.
# Класс BankAccount должен отражать банковский счет с балансом и методами для пополнения и снятия денег.
# Необходимо использовать механизм блокировки,
# чтобы избежать проблемы гонок (race conditions) при модификации общего ресурса.

# Используйте класс Lock из модуля threading для блокировки доступа к общему ресурсу.
# Ожидается создание двух потоков, один для пополнения счета, другой для снятия денег.
# Используйте with (lock object): в начале каждого метода, чтобы использовать блокировку


# Решение:
from threading import Thread, Lock


class BankAccount:
    lock = Lock()

    def __init__(self, amount=0):
        self.amount = amount

    def deposit(self, amount):
        with self.lock:
            self.amount += amount
            print(f'Deposited {amount}, new balance is {self.amount}')

    def withdraw(self, amount):
        with self.lock:
            self.amount -= amount
            print(f'Withdrew {amount}, new balance is {self.amount}')


def deposit_task(account, amount):
    for _ in range(5):
        account.deposit(amount)


def withdraw_task(account, amount):
    for _ in range(5):
        account.withdraw(amount)


# Проверка:
account = BankAccount(1000)
deposit_thread = Thread(target=deposit_task, args=(account, 100))
withdraw_thread = Thread(target=withdraw_task, args=(account, 150))

deposit_thread.start()
withdraw_thread.start()

deposit_thread.join()
withdraw_thread.join()