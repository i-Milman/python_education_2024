# Задача "Продуктовая база":
# Подготовка:
# Для решения этой задачи вам понадобится код из предыдущей задачи. Дополните его, следуя пунктам задачи ниже.
#
# Дополните ранее написанный код для Telegram-бота:
# Создайте файл crud_functions.py и напишите там следующие функции:
# initiate_db, которая создаёт таблицу Products, если она ещё не создана при помощи SQL запроса.
# Эта таблица должна содержать следующие поля:
# id - целое число, первичный ключ
# title(название продукта) - текст (не пустой)
# description(описание) - тест
# price(цена) - целое число (не пустой)
# get_all_products, которая возвращает все записи из таблицы Products, полученные при помощи SQL запроса.
#
# Изменения в Telegram-бот:
# В самом начале запускайте ранее написанную функцию get_all_products.
# Измените функцию get_buying_list в модуле с Telegram-ботом,
# используя вместо обычной нумерации продуктов функцию get_all_products.
# Полученные записи используйте в выводимой надписи: "Название: <title> | Описание: <description> | Цена: <price>"
# Перед запуском бота пополните вашу таблицу Products 4 или более записями для последующего вывода в чате Telegram-бота.

# Решение:
# python 3.11.9 | aiogram 3.12.0
import asyncio
import logging
import sys

from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart
from aiogram.types import Message, CallbackQuery, FSInputFile

from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder

from crud_functions import *

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


# Клавиатуры
def kb_menu(text: str | list):
    """
    Унифицированная система создания меню
    :param text: Тексты кнопок
    :return: Маркап для использования в сообщении
    """
    builder = ReplyKeyboardBuilder()
    if isinstance(text, str):
        text = [text]
    [builder.button(text=txt) for txt in text]
    return builder.as_markup(resize_keyboard=True, one_time_keyboard=True)


def ikb_menu(text: str | list):
    """
    Унифицированная система создания инлайн-меню
    :param text: Тексты кнопок
    :return: Маркап для использования в сообщении
    """
    builder = InlineKeyboardBuilder()
    if isinstance(text, str):
        text = [text]
    [builder.button(text=txt, callback_data=txt) for txt in text]
    return builder.as_markup()


builder = InlineKeyboardBuilder()
[builder.button(text=f'Product{i}', callback_data='product_buying') for i in range(1, 5)]
ikb_buy_menu = builder.as_markup()


# Обработчики команд
@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    """
    Этот обработчик получает сообщения с помощью команды `/start`
    """
    await message.answer("Привет! Я бот помогающий твоему здоровью.",
                         reply_markup=kb_menu(['Рассчитать', 'Информация', 'Купить']))


# Обработчики команд без префикса
@dp.message(F.text.lower().startswith('рассчитать'))
async def main_menu(message: Message) -> None:
    """
    Этот обработчик получает сообщения с помощью команды `рассчитать`
    """
    await message.answer("Выберите опцию:",
                         reply_markup=ikb_menu(['Рассчитать норму калорий', 'Формулы расчёта']))


@dp.message(F.text.lower().startswith('купить'))
async def get_buying_list(message: Message) -> None:
    products = get_all_products()
    for i in range(len(products)):
        await message.answer(f'Название: {products[i][1]} | Описание: {products[i][2]} | Цена: {products[i][3]}')
        await message.answer_photo(FSInputFile('product.webp'))
    await message.answer('Выберите продукт для покупки:', reply_markup=ikb_buy_menu)


# Обработчики нажатий на инлайн-кнопки
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


@dp.callback_query(F.data == 'product_buying')
async def buy(callback: CallbackQuery) -> None:
    await callback.message.answer('Вы успешно приобрели продукт!')
    await callback.answer()


# Обработчики состояний
@dp.message(UserState.age)
async def set_age(message: Message, state: FSMContext) -> None:
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
async def set_growth(message: Message, state: FSMContext) -> None:
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
async def set_weight(message: Message, state: FSMContext) -> None:
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
    logging.basicConfig(level=logging.INFO, stream=sys.stdout,
                        format='%(asctime)s | %(message)s')
    asyncio.run(main())
