from app.config import *


async def start(message: types.Message, state: FSMContext):
    await state.finish()
    if message.chat.id not in users:
        users.append(message.chat.id)
        logger.info("Пользователь {0} (id: {1}) подписался".format(message.from_user.username, message.from_user.id))
    await message.answer("Тебя приветствует бот для заданий канала...")


async def cancel(message: types.Message, state: FSMContext):
    await state.finish()
    await message.answer("Действие было отменено")


def register_handlers_common(dp: Dispatcher):
    dp.register_message_handler(start, commands="start", state="*")
    dp.register_message_handler(cancel, commands="cancel", state="*")
