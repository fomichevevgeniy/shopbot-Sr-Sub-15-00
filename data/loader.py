from aiogram import Bot, Dispatcher, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from database.database import DataBase
bot = Bot('5483050351:AAEsECspsYimZjvwsG-6vgYrb41CEV73SbQ', parse_mode='HTML')

db = DataBase()
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)