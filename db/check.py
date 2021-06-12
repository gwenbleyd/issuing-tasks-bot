import sqlite3
from app.config import *


def is_user(user_id):
    try:
        sqlite_connection = sqlite3.connect('botDB.db')
        sqlite_query = "select id from users where id = {};".format(user_id)
        cursor = sqlite_connection.cursor()
        if not cursor.execute(sqlite_query).fetchall():
            cursor.close()
            return 0
        else:
            cursor.close()
            return 1

    except sqlite3.Error as error:
        logger.error("(is_user) Ошибка: {}".format(error.args))
    finally:
        if sqlite_connection:
            sqlite_connection.close()
            logger.info("(is_user) Соединение с SQLite закрыто")


def is_admin(amin_id):
    pass


def is_task(number):
    pass
