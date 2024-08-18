# Задача "Цепочка вопросов":
# Необходимо сделать цепочку обработки состояний для нахождения нормы калорий для человека.
# Группа состояний:
#     Импортируйте классы State и StateGroup из aiogram.dispatcher.filters.state.
#     Создайте класс UserState наследованный от StateGroup.
#     Внутри этого класса опишите 3 объекта класса State: age, growth, weight (возраст, рост, вес).
#     Эта группа(класс) будет использоваться в цепочке вызовов message_handler'ов.
# Напишите следующие функции для обработки состояний:
#     Функцию set_age(message):
#         Оберните её в message_handler, который реагирует на текстовое сообщение 'Calories'.
#         Эта функция должна выводить в Telegram-бот сообщение 'Введите свой возраст:'.
#         После ожидать ввода возраста в атрибут UserState.age при помощи метода set.
#     Функцию set_growth(message, state):
#         Оберните её в message_handler, который реагирует на переданное состояние UserState.age.
#         Эта функция должна обновлять данные в состоянии age на message.text (написанное пользователем сообщение).
#         Используйте метод update_data.
#         Далее должна выводить в Telegram-бот сообщение 'Введите свой рост:'.
#         После ожидать ввода роста в атрибут UserState.growth при помощи метода set.
#     Функцию set_weight(message, state):
#         Оберните её в message_handler, который реагирует на переданное состояние UserState.growth.
#         Эта функция должна обновлять данные в состоянии growth на message.text (написанное пользователем сообщение).
#         Используйте метод update_data.
#         Далее должна выводить в Telegram-бот сообщение 'Введите свой вес:'.
#         После ожидать ввода роста в атрибут UserState.weight при помощи метода set.
#     Функцию send_calories(message, state):
#         Оберните её в message_handler, который реагирует на переданное состояние UserState.weight.
#         Эта функция должна обновлять данные в состоянии weight на message.text (написанное пользователем сообщение).
#         Используйте метод update_data.
#         Далее в функции запомните в переменную data все ранее введённые состояния при помощи state.get_data().
#         Используйте упрощённую формулу Миффлина - Сан Жеора для подсчёта нормы калорий
#         (для женщин или мужчин - на ваше усмотрение).
#         Данные для формулы берите из ранее объявленной переменной data по ключам age, growth и weight соответственно.
#         Результат вычисления по формуле отправьте ответом пользователю в Telegram-бот.
# Финишируйте машину состояний методом finish().
# !В течение написания этих функций помните, что они асинхронны и все функции
# и методы должны запускаться с оператором await.

# Решение:
# python 3.11.9 | aiogram 3.10.0
import asyncio
import logging
import sys

from aiogram import Bot, Dispatcher
from aiogram.filters import Command, CommandStart
from aiogram.types import Message

from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext

# Токен бота
with open("token.txt") as f:
    TOKEN = f.read().strip()

# Инициализация бота
bot = Bot(token=TOKEN)

# Все обработчики должны быть подключены к маршрутизатору (или Диспетчеру)
dp = Dispatcher()


class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()


# Обработчик команды '/start'
@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    """
    Этот обработчик получает сообщения с помощью команды `/start`
    """
    await message.answer("Привет! Я бот помогающий твоему здоровью.")


@dp.message(Command('Calories'))
async def set_age(message: Message, state: FSMContext) -> None:
    await state.set_state(UserState.age)
    await message.answer("Введите свой возраст:")


@dp.message(UserState.age)
async def set_age(message: Message, state: FSMContext):
    if message.text.isdigit():
        await state.update_data(age=message.text)
        await state.set_state(UserState.growth)
        await message.answer("Введите свой рост:")
    else:
        await message.answer('Введите число, еще раз:')


@dp.message(UserState.growth)
async def set_growth(message: Message, state: FSMContext):
    if message.text.isdigit():
        await state.update_data(growth=message.text)
        await state.set_state(UserState.weight)
        await message.answer("Введите свой вес:")
    else:
        await message.answer('Введите число, еще раз:')


@dp.message(UserState.weight)
async def set_weight(message: Message, state: FSMContext):
    if message.text.isdigit():
        await state.update_data(weight=message.text)
        await state.set_state(UserState.growth)

        data = await state.get_data()
        await state.clear()

        result = float(data["weight"]) * 10 + float(data["growth"]) * 6.25 - float(data["age"]) * 5 + 5
        await message.answer(f'Ваша норма калорий: {result}')
    else:
        await message.answer('Введите число, еще раз:')


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
