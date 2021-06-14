from db.check import *
from db.add import *


async def start(message: types.Message, state: FSMContext):
    await state.finish()
    if not await is_user(message.chat.id):
        await add_user(message.from_user.id, message.from_user.username)
    await message.answer("Тебя приветствует бот для заданий канала...")


async def cancel(message: types.Message, state: FSMContext):
    await state.finish()
    await message.answer("Действие было отменено")


def register_handlers_common(dp: Dispatcher):
    dp.register_message_handler(start, commands="start", state="*")
    dp.register_message_handler(cancel, commands="cancel", state="*")
