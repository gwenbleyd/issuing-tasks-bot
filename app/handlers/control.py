from app.config import *


async def post(message: types.Message):
    print(message)
    if message.from_user.id == MAIN_CHAT_ID:
        logger.info("Добавлено новое задание")
        msgs.append(message.forward_from_message_id)
    elif message.chat.id == GROUP_ID and message.reply_to_message.forward_from_message_id in msgs:
        logger.info(
            "Пользователь {} (id: {}) ответил на задание {}".format(message.from_user.username, message.from_user.id,
                                                                    message.reply_to_message.forward_from_message_id))
        if message.from_user.id in users:
            await bot.send_message(message.from_user.id, "Конетент")


def register_handlers_control(dp: Dispatcher):
    dp.register_message_handler(post, content_types=['document', 'photo', 'text'], state='*')