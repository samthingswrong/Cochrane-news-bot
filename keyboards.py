from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, \
    ReplyKeyboardMarkup, KeyboardButton


button_hi = KeyboardButton('Hi! 👋')
greet_kb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
greet_kb.add(button_hi)

inline_button_link = InlineKeyboardButton(text='More information... 👨‍🔬')
inline_kb_link = InlineKeyboardMarkup().add(inline_button_link)
