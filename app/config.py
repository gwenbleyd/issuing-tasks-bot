from aiogram import Bot, Dispatcher, executor, types
import logging
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext

TOKEN = '1804068546:AAGxAbE5ArBkl3hmlRn8YQfaSgtuqo7iL9Q'
CHAT_ID = '@test_for_bot_chan'
MAIN_CHAT_ID = 777000
GROUP_ID = -1001386327684
bot = Bot(token=TOKEN)
logger = logging.getLogger(__name__)
msg_task = types.message
msgs = list()
users = list()
SUPER_USER_ID = 447959709
admins = list()
admins.append(SUPER_USER_ID)


def is_admin(message):
    if message.chat.id in admins:
        return 1
    else:
        return 0
