from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
import asyncio    #import django print(django.get_version())

class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()

api = " "
bot = Bot(token = api)
dp = Dispatcher(bot, storage = MemoryStorage())
kb = ReplyKeyboardMarkup()
button = KeyboardButton(text="Рассчитать")
b2 = KeyboardButton(text='Информация')
kb.add(button)
kb.insert(b2)

@dp.message_handler(commands = ['start'])
async def start_message(message):
    await message.answer("Привет!", reply_markup = kb)

@dp.message_handler(text = "Информация")
async def inform(message):
    await message.answer("Информация о боте")


@dp.message_handler(text = "Рассчитать")
async def set_age(message):
    await message.answer("Введите свой возраст:")
    await UserState.age.set()

@dp.message_handler(state = UserState.age)
async def set_growth(message, state):
    await state.update_data(age = message.text)
    await message.answer("Введите свой рост:")
    await UserState.growth.set()

@dp.message_handler(state = UserState.growth)
async def set_weight(message, state):
    await state.update_data(growth = message.text)
    await message.answer("Введите свой вес: ")
    await UserState.weight.set()

@dp.message_handler(state = UserState.weight)
async def send_calories(message, state):
    await state.update_data(weight = message.text)
    data = await state.get_data()
    await message.answer(f"По упрощенной формуле Миффлина-Сан Жеора расчет калорий даёт: {10*int(data['weight'])+6.25*int(data['growth'])-5*int(data['age'])}")
    await state.finish()

@dp.message_handler()
async def all_message(message):
    await message.answer('Введите команду /start, чтобы начать общение.')

executor.start_polling(dp, skip_updates = True)