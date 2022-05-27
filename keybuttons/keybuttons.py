from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

start = KeyboardButton('/start')
kb_client_start = ReplyKeyboardMarkup(resize_keyboard=True)
kb_client_start.add(start)

gotov = KeyboardButton('/Готов')
negotov = KeyboardButton('/Не_готов')
kb_gotov = ReplyKeyboardMarkup(resize_keyboard=True)
kb_gotov.add(gotov).add(negotov)
