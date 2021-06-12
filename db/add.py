from app.config import *


def add_user(user_id, nickname):
    try:
        sqlite_connection = sqlite3.connect('botDB.db')
        cursor = sqlite_connection.cursor()
        cursor.execute("insert into users (id, nickname) values (?, ?)", (user_id, nickname))
        sqlite_connection.commit()
        logger.info("Пользователь {0} (id: {1}) подписался".format(nickname, user_id))
        cursor.close()
    except sqlite3.Error as error:
        logger.error("(add_user) Ошибка: {}".format(error.args))
    finally:
        if sqlite_connection:
            sqlite_connection.close()
            logger.info("Соединение с SQLite закрыто")


def add_admin(user_id, nickname):
    try:
        sqlite_connection = sqlite3.connect('botDB.db')
        cursor = sqlite_connection.cursor()
        cursor.execute("insert into admins (id, nickname) values (?, ?)", (user_id, nickname))
        sqlite_connection.commit()
        logger.info("Пользователь {0} (id: {1}) стал администратором".format(nickname, user_id))
        cursor.close()
    except sqlite3.Error as error:
        logger.error("(add_admin) Ошибка: {}".format(error.args))
    finally:
        if sqlite_connection:
            sqlite_connection.close()
            logger.info("Соединение с SQLite закрыто")
    pass


def add_msg(number):
    try:
        sqlite_connection = sqlite3.connect('botDB.db')
        cursor = sqlite_connection.cursor()
        cursor.execute("insert into message (number) values (?)", number)
        sqlite_connection.commit()
        logger.info("Было добавлено задание №{}".format(number))
        cursor.close()
    except sqlite3.Error as error:
        logger.error("(add_msg) Ошибка: {}".format(error.args))
    finally:
        if sqlite_connection:
            sqlite_connection.close()
            logger.info("Соединение с SQLite закрыто")
    pass
