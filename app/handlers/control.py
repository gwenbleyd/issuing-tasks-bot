from db.check import *
from db.add import *


async def post(message: types.Message):
    print(message)
    if message.from_user.id == MAIN_CHAT_ID:
        add_msg(message.forward_from_message_id)
    elif message.chat.id == GROUP_ID and is_task( message.reply_to_message.forward_from_message_id):
        logger.info(
            "Пользователь {} (id: {}) ответил на задание {}".format(message.from_user.username, message.from_user.id,
                                                                    message.reply_to_message.forward_from_message_id))
        if not is_user(message.from_user):
            await bot.send_message(message.from_user.id, "Контент")


def register_handlers_control(dp: Dispatcher):
    dp.register_message_handler(post, content_types=['document', 'photo', 'text'], state='*')