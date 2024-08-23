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

from aiogram import Bot, Dispatcher, F
from aiogram.filters import Command, CommandStart
from aiogram.types import Message, CallbackQuery

from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder

# Токен бота
with open("token.txt") as f:
    TOKEN = f.read().strip()

# Инициализация бота
bot = Bot(token=TOKEN)

# Все обработчики должны быть подключены к маршрутизатору (или Диспетчеру)
dp = Dispatcher()


# Состояния
class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()


# Кнопки
def kb_menu(text: str | list):
    builder = ReplyKeyboardBuilder()
    if isinstance(text, str):
        text = [text]
    [builder.button(text=txt) for txt in text]
    return builder.as_markup(resize_keyboard=True, one_time_keyboard=True)


def kb_inline_menu(text: str | list):
    builder = InlineKeyboardBuilder()
    if isinstance(text, str):
        text = [text]
    [builder.button(text=txt, callback_data=txt) for txt in text]
    return builder.as_markup(resize_keyboard=True)


# Обработчик команды '/start'
@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    """
    Этот обработчик получает сообщения с помощью команды `/start`
    """
    await message.answer("Привет! Я бот помогающий твоему здоровью.",
                         reply_markup=kb_menu(['Рассчитать', 'Информация']))


@dp.message(F.text.lower() == 'рассчитать')
async def main_menu(message: Message) -> None:
    """
    Этот обработчик получает сообщения с помощью команды `рассчитать`
    """
    await message.answer("Выберите опцию:",
                         reply_markup=kb_inline_menu(['Рассчитать норму калорий', 'Формулы расчёта']))


@dp.callback_query(F.data == 'Формулы расчёта')
async def callback_query_handler(callback: CallbackQuery) -> None:
    """
    Этот обработчик запускается с помощью инлайн-кнопки `Формулы расчёта`
    """
    await callback.message.answer("10 х вес (кг) + 6,25 x рост (см) – 5 х возраст (г) + 5")
    await callback.answer()


@dp.callback_query(F.data == 'Рассчитать норму калорий')
async def start_calc(callback: CallbackQuery, state: FSMContext) -> None:
    """
    Этот обработчик запускается с помощью инлайн-кнопки `Рассчитать норму калорий`
    """
    await state.set_state(UserState.age)
    await callback.message.answer("Введите свой возраст:")
    await callback.answer()


@dp.message(UserState.age)
async def set_age(message: Message, state: FSMContext):
    """
    Этот обработчик запускается с помощью состояния `UserState.age`
    """
    if message.text.isdigit():
        await state.update_data(age=message.text)
        await state.set_state(UserState.growth)
        await message.answer("Введите свой рост:")
    else:
        await message.answer('Введите число, еще раз:')


@dp.message(UserState.growth)
async def set_growth(message: Message, state: FSMContext):
    """
    Этот обработчик запускается с помощью состояния `UserState.growth`
    """
    if message.text.isdigit():
        await state.update_data(growth=message.text)
        await state.set_state(UserState.weight)
        await message.answer("Введите свой вес:")
    else:
        await message.answer('Введите число, еще раз:')


@dp.message(UserState.weight)
async def set_weight(message: Message, state: FSMContext):
    """
    Этот обработчик запускается с помощью состояния `UserState.weight`
    """
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
    Обработчик переадресует полученное сообщение обратно отправителю,
    запускается, если не был вызван другой обработчик
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
