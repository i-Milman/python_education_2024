# К коду из подготовительного видео напишите две асинхронные функции:
# start(message) - печатает строку в консоли 'Привет! Я бот помогающий твоему здоровью.' .
#   Запускается только когда написана команда '/start' в чате с ботом. (используйте соответствующий декоратор)
# all_massages(message) - печатает строку в консоли 'Введите команду /start, чтобы начать общение.'.
#   Запускается при любом обращении не описанном ранее. (используйте соответствующий декоратор)
# Запустите ваш Telegram-бот и проверьте его на работоспособность.

# Решение:
# python 3.11.9 | aiogram 3.10.0
import asyncio
import logging
import sys

from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart
from aiogram.types import Message


# Токен бота
with open("token.txt") as f:
    TOKEN = f.read().strip()

# Инициализация бота
bot = Bot(token=TOKEN)

# Все обработчики должны быть подключены к маршрутизатору (или Диспетчеру)
dp = Dispatcher()


# Обработчик команды '/start'
@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    """
    Этот обработчик получает сообщения с помощью команды `/start`
    """
    await message.answer("Привет! Я бот помогающий твоему здоровью.")


# Обработчик любого текстового сообщения
@dp.message()
async def echo_handler(message: Message) -> None:
    """
    Обработчик переадресует полученное сообщение обратно отправителю
    """
    await message.answer("Введите команду /start, чтобы начать общение.")


async def main() -> None:
    """
    Запуск Диспетчера событий
    """
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
