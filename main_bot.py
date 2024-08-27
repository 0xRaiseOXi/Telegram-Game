import asyncio
import logging
import time
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command
from main_message import *
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.filters import Text
from BASE_DATA import connect, cur

logging.basicConfig(level=logging.INFO)
bot = Bot(token='5873733556:AAFjsgaNJNt3aSzbtghpYN9vlqgUoqPjjBA')
dp = Dispatcher()

@dp.message(Command("start"))
async def main_start(message: types.Message):
    await message.answer("Ура я работаю на vds!")
    buider = InlineKeyboardBuilder()
    buider.add(types.InlineKeyboardButton(
     text="Начинаем!",
        callback_data = "main")
    )
    await message.answer(
        cmd_main(), 
        reply_markup=buider.as_markup()
    )


@dp.callback_query(Text("main"))
async def main_subviliom_start(callback: types.CallbackQuery):
    buttons = [
        [
            types.InlineKeyboardButton(text="Ксионония-->", callback_data="ksiononia")
        ],
        [types.InlineKeyboardButton(text="Выбрать", callback_data="start_aurantis")]
    ]
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=buttons)
    await callback.message.edit_text(aurantis(), reply_markup=keyboard)
    await callback.answer()

@dp.callback_query(Text("ksiononia"))
async def cmd_ksiononia(callback: types.CallbackQuery):
    buttons = [
        [
            types.InlineKeyboardButton(text="<--Аурантис", callback_data="main"),
            types.InlineKeyboardButton(text="Новаэрис-->", callback_data="novaeris")
        ],
        [types.InlineKeyboardButton(text="Выбрать", callback_data="start_ksiononia")]
    ]
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=buttons)
    await callback.message.edit_text(ksionia(), reply_markup=keyboard)
    await callback.answer()
    
@dp.callback_query(Text("novaeris"))
async def cmd_novaeris(callback: types.CallbackQuery):
    buttons = [
        [
            types.InlineKeyboardButton(text="<--Ксионония", callback_data="ksiononia"),
        ],
        [types.InlineKeyboardButton(text="Выбрать", callback_data="start_novaeris")]
    ]
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=buttons)
    await callback.message.edit_text(novaeris(), reply_markup=keyboard)
    await callback.answer()

@dp.callback_query(Text("start_aurantis"))
async def start_aurantis(callback: types.CallbackQuery):
    buttons = [
        [
            types.InlineKeyboardButton(text="Подтвердить", callback_data="main_start")
        ],
        [types.InlineKeyboardButton(text="Назад", callback_data="main")]
    ]
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=buttons)
    await callback.message.edit_text(start_aurantis_text(), reply_markup=keyboard)


@dp.callback_query(Text("start_ksiononia"))
async def start_aurantis(callback: types.CallbackQuery):
    buttons = [
        [
            types.InlineKeyboardButton(text="Подтвердить", callback_data="main_start")
        ],
        [types.InlineKeyboardButton(text="Назад", callback_data="main")]
    ]
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=buttons)
    await callback.message.edit_text(start_ksiononia_text(), reply_markup=keyboard)


@dp.callback_query(Text("start_novaeris"))
async def start_aurantis(callback: types.CallbackQuery):
    buttons = [
        [
            types.InlineKeyboardButton(text="Подтвердить", callback_data="main_start")
        ],
        [types.InlineKeyboardButton(text="Назад", callback_data="main")]
    ]
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=buttons)
    await callback.message.edit_text(start_novaeris_text(), reply_markup=keyboard)



@dp.callback_query(Text('main_menu_novaeris'))
async def main_trigger_menu(callback: types.CallbackQuery):
    #buttons =
    await callback.message.edit_text("""Subviliom База игрока 
______________________________
Общая мощь: 
Баланс:
Энергия:
Производство:

Век: 
Уровень: 
_______________________________""") 
    

@dp.callback_query(Text('main_start'))
async def main_trigger_menu(callback: types.CallbackQuery):
    buttons = [
        [
            types.InlineKeyboardButton(text="Продолжить", callback_data="call_capitan")
        ]
    ]
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=buttons)
    await callback.message.edit_text("""QA Лаборатория 

Запуск всех систем функционирования...""")
    time.sleep(2)
    await callback.message.edit_text("""QA Лаборатория 

Запуск всех систем функционирования...
Война закончилась. Мы смогли последними силами остановить врага. Наш центр остался нетронутым.
Я бы сказал нам очень повезло, но благодаря тем кораблям, которые были уничтожены бесследно, мы остались в покое.

Капитан, с вами хочет связаться командир станции ZetX...
""")
    time.sleep(5)
    await callback.message.edit_text("""QA Лаборатория 

Запуск всех систем функционирования...
Война закончилась. Мы смогли последними силами остановить врага. Наш центр остался нетронутым.
Я бы сказал нам очень повезло, но благодаря тем кораблям, которые были уничтожены бесследно, мы остались в покое.

Капитан, с вами хочет связаться командир станции ZetX...
""", reply_markup=keyboard)



async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())

