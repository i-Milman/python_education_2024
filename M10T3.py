# Задача:
# Реализуйте программу, которая имитирует доступ к общему ресурсу с использованием механизма блокировки потоков.
# Класс BankAccount должен отражать банковский счет с балансом и методами для пополнения и снятия денег.
# Необходимо использовать механизм блокировки,
# чтобы избежать проблемы гонок (race conditions) при модификации общего ресурса.

# Решение:
from threading import Thread, Lock


class BankAccount(Thread):

    def __init__(self, *args, **kwargs):
        super(BankAccount, self).__init__(*args, **kwargs)


def deposit_task(account, amount):
    for _ in range(5):
        account.deposit(amount)

def withdraw_task(account, amount):
    for _ in range(5):
        account.withdraw(amount)
        account = BankAccount()

# Проверка:
deposit_thread = threading.Thread(target=deposit_task, args=(account, 100))
withdraw_thread = threading.Thread(target=withdraw_task, args=(account, 150))

deposit_thread.start()
withdraw_thread.start()

deposit_thread.join()
withdraw_thread.join()

# Deposited 100, new balance is 1100
# Deposited 100, new balance is 1200
# Deposited 100, new balance is 1300
# Deposited 100, new balance is 1400
# Deposited 100, new balance is 1500
# Withdrew 150, new balance is 1350
# Withdrew 150, new balance is 1200
# Withdrew 150, new balance is 1050
# Withdrew 150, new balance is 900
# Withdrew 150, new balance is 750