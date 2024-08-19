# Задача "Меньше текста, больше кликов":
# Необходимо дополнить код предыдущей задачи, чтобы вопросы о параметрах тела
# для расчёта калорий выдавались по нажатию кнопки.
# Измените massage_handler для функции set_age. Теперь этот хэндлер будет реагировать на текст 'Рассчитать',
# а не на 'Calories'.
# Создайте клавиатуру ReplyKeyboardMarkup и 2 кнопки KeyboardButton на ней со следующим текстом: 'Рассчитать'
# и 'Информация'. Сделайте так, чтобы клавиатура подстраивалась под размеры интерфейса устройства
# при помощи параметра resize_keyboard.
# Используйте ранее созданную клавиатуру в ответе функции start, используя параметр reply_markup.
# В итоге при команде /start у вас должна присылаться клавиатура с двумя кнопками. При нажатии на кнопку
# с надписью 'Рассчитать' срабатывает функция set_age с которой начинается работа машины состояний
# для age, growth и weight.

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
from aiogram.utils.keyboard import ReplyKeyboardBuilder

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


def kb_main_menu(text: str | list):
    builder = ReplyKeyboardBuilder()
    if isinstance(text, str):
        text = [text]
    [builder.button(text=txt) for txt in text]
    return builder.as_markup(resize_keyboard=True, one_time_keyboard=True)


# Обработчик команды '/start'
@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    """
    Этот обработчик получает сообщения с помощью команды `/start`
    """
    await message.answer("Привет! Я бот помогающий твоему здоровью.",
                         reply_markup=kb_main_menu(['/Calories', '/Information']))


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
