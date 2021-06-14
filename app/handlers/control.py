from db.check import *
from db.add import *


async def post(message: types.Message):
    if message.from_user.id == int(MAIN_CHAT_ID):
        await add_msg(message.forward_from_message_id)
    elif message.chat.id == int(GROUP_ID):
        if await is_task(message.reply_to_message.forward_from_message_id):
            if await is_user(message.from_user.id):
                logger.info(
                    "Пользователь {} (id: {}) ответил на задание {}".format(
                        message.from_user.username,
                        message.from_user.id,
                        message.reply_to_message.forward_from_message_id
                    )
                )
                await bot.send_message(message.from_user.id, "Контент")


def register_handlers_control(dp: Dispatcher):
    dp.register_message_handler(post, content_types=['document', 'photo', 'text'], state='*')
