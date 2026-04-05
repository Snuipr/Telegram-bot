
import database as db
from aiogram.types import (ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton,
                           InlineKeyboardButton, InlineKeyboardMarkup)



def start(id: int):
    try:
        #status = "Подтвеждено" if db.info(id)["phone"] else "Необходимо ввести номер телефона"
        status = "Подтверждено"
        return InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text=status, callback_data="contact")],
                                                     [InlineKeyboardButton(text="Получить данные аккаунта iCloud", callback_data="account")],
                                                     [InlineKeyboardButton(text="Инструкция", callback_data="helper")],
                                                     [InlineKeyboardButton(text="Поддержка", callback_data="support")]])
    except Exception as e:
        raise e




contact = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text="Отправить свой контакт ☎️", request_contact=True)],
                                        [KeyboardButton(text="Ввести номер вручную")]], resize_keyboard=True, one_time_keyboard=True)






