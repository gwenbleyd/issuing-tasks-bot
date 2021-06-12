from db.check import *


class TaskState(StatesGroup):
    needImg = State()
    addImg = State()


def get_keyboard():
    buttons = [
        types.InlineKeyboardButton(text="Да", callback_data="yes"),
        types.InlineKeyboardButton(text="Нет", callback_data="no"),
        types.InlineKeyboardButton(text="Отмена", callback_data="cancel")
    ]
    keyboard = types.InlineKeyboardMarkup(row_width=2)
    keyboard.add(*buttons)
    return keyboard


async def add_task(message: types.Message):
    if is_admin(message):
        await message.answer("Введи текст задания!")
        await TaskState.needImg.set()


async def choice_yes(call: types.CallbackQuery):
    await call.message.answer("Пришли картинку")
    await call.answer()
    await call.message.delete_reply_markup()
    await TaskState.addImg.set()


async def choice_no(call: types.CallbackQuery):
    await bot.send_message(chat_id=CHAT_ID, text=msg_task.text)
    await call.answer(text="Новое задание добавлено!")
    logger.info('Администратор {} добавил новое задание'.format(call.message.chat.id))
    await call.answer()
    await call.message.delete_reply_markup()


async def choice_cancel(call: types.CallbackQuery, state: FSMContext):
    await state.finish()
    await call.answer(show_alert=False, text="Добавление задания отменено")
    await call.answer()
    await call.message.delete_reply_markup()


async def process_choice_img(message: types.Message, state: FSMContext):
    global msg_task
    msg_task = message
    await message.answer("Нужна ли картинка?", reply_markup=get_keyboard())
    await state.finish()


async def process_link_img(message: types.Message, state: FSMContext):
    await bot.send_photo(CHAT_ID, str(message.photo[0].file_id), caption=msg_task.text)
    await message.answer(text="Новое задание добавлено!")
    logger.info('Администратор {} добавил новое задание'.format(message.chat.id))
    await state.finish()


def register_handlers_task(dp: Dispatcher):
    dp.register_message_handler(add_task, commands='task', state='*')
    dp.register_callback_query_handler(choice_no, text_contains="no")
    dp.register_callback_query_handler(choice_yes, text_contains="yes")
    dp.register_callback_query_handler(choice_cancel, text_contains="cancel", state='*')
    dp.register_message_handler(process_choice_img, content_types=['text'], state=TaskState.needImg)
    dp.register_message_handler(process_link_img, content_types=['document', 'photo'], state=TaskState.addImg)