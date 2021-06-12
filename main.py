from app.config import *
from app.handlers.admin import register_handlers_admin
from app.handlers.common import register_handlers_common
from app.handlers.task import register_handlers_task
from app.handlers.control import register_handlers_control

if __name__ == '__main__':
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(name)s - %(message)s",
    )
    logger.info("Starting bot")

    dp = Dispatcher(bot, storage=MemoryStorage())

    register_handlers_admin(dp)
    register_handlers_common(dp)
    register_handlers_task(dp)
    register_handlers_control(dp)

    executor.start_polling(dp, skip_updates=True)