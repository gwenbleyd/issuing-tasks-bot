from db.check import *
from db.add import *

# def get_keyboard():
#     buttons = [
#         types.InlineKeyboardButton(text="Добавить", callback_data="add"),
#         types.InlineKeyboardButton(text="Удалить", callback_data="del"),
#         types.InlineKeyboardButton(text="Отмена", callback_data="cncl")
#     ]
#     keyboard = types.InlineKeyboardMarkup(row_width=2)
#     keyboard.add(*buttons)
#     return keyboard
#
#
# class AdminState(StatesGroup):
#     add = State()
#     delete = State()
#
#
# async def control(message: types.Message):
#     if int(message.chat.id) == SUPER_USER_ID:
#         await message.answer("Что хотите сделать?", reply_markup=get_keyboard())
#
#
# async def choice_add(call: types.CallbackQuery):
#     await call.message.answer("Введи id того, кого хочешь сделать админстратором")
#     await call.answer()
#     await call.message.delete_reply_markup()
#     await AdminState.add.set()
#
#
# async def choice_delete(call: types.CallbackQuery):
#     await call.message.answer("Введи id того, кого хочешь удалить из админстратором")
#     await call.answer()
#     await call.message.delete_reply_markup()
#     await AdminState.delete.set()
#
#
# async def choice_cancel(call: types.CallbackQuery):
#     await call.answer(show_alert=False, text="Действие отменено")
#     logger.info("Администратор {} отменил свое действие".format(call.message.chat.id))
#     await call.answer()
#     await call.message.delete_reply_markup()
#
#
# async def process_add_admin_step(message: types.Message, state: FSMContext):
#     if int(message.text) not in admins:
#         admins.append(int(message.text))
#         await message.answer('Администратор добавлен')
#         logger.info('Администратор {} добавил нового администратора: {}'.format(message.chat.id, message.text))
#         await state.finish()
#     else:
#         await state.finish()
#
#
# async def process_delete_admin_step(message: types.Message, state: FSMContext):
#     if int(message.text) in admins:
#         admins.remove(int(message.text))
#         await message.answer('Администратор удален')
#         logger.info('Администратор {} удалил администратора {}'.format(message.chat.id, message.text))
#         await state.finish()
#     else:
#         await state.finish()


async def help_message(message: types.Message):
    if is_admin(message.from_user.id):
        await message.answer("Для администратора предусмторены следующие функции...")


def register_handlers_admin(dp: Dispatcher):
#     dp.register_message_handler(control, commands='admin', state='*')
#     dp.register_callback_query_handler(choice_add, text_contains="add")
#     dp.register_callback_query_handler(choice_delete, text_contains="del")
#     dp.register_callback_query_handler(choice_cancel, text_contains="cncl")
#     dp.register_message_handler(process_add_admin_step, state=AdminState.add)
#     dp.register_message_handler(process_delete_admin_step, state=AdminState.delete)
    dp.register_message_handler(help_message, commands='help', state='*')