
import asyncio
import config as cfg
import keyboard as kb
from aiogram import F, Bot, Dispatcher
from aiogram.types import Message, CallbackQuery
from aiogram.filters import Command



bot = Bot(token=cfg.bot_token)

ds = Dispatcher()

@ds.message(Command("start"))
async def start(message: Message):
    try:
        name = message.from_user.first_name+" "+message.from_user.last_name
        await message.answer(text=f"Привет {name}", reply_markup=kb.start(message.from_user.id))
    except Exception as e:
        raise e

@ds.message(lambda message: message.contact is not None)
async def auto_phone(message: Message):
    contact = message.contact
    phone = contact.phone_number
    await message.answer(text=f"Номер {phone}")

@ds.message(lambda message: message.text.isdigit())
async def phone(message: Message):
    if len(message.text) == 11 and int(message.text[0]) in [7, 8]:
        await message.answer(text=f"Это похоже на номер +{message.text}")


@ds.callback_query(F.data == "contact")
async def contact(callback: CallbackQuery):
    try:
        await callback.answer()
    except Exception as e:
        raise e








async def main():
    await ds.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())