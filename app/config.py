from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
import os
import sqlite3

import logging

TOKEN = os.getenv("TOKEN")
CHAT_ID = os.getenv("CHAT_ID")
MAIN_CHAT_ID = os.getenv("MAIN_CHAT_ID")
GROUP_ID = os.getenv("GROUP_ID")

bot = Bot(token=TOKEN)

logger = logging.getLogger(__name__)

msg_task = types.message

SUPER_USER_ID = 447959709
