import telebot
import datetime
import sqlite3
import re

class DataBase:
    def __init__(self, db_name):
        self.db_name = db_name
        self.__create_table()

    def __create_table(self):
        sql = self.connect_db()
        sql['cursor'].execute('''
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER        PRIMARY     KEY AUTOINCREMENT, 
                id_telegram       INTEGER     NOT NULL UNIQUE,
                username          TEXT,
                first_name        TEXT,
                last_name         TEXT,
                date_reqistration DATE,
                access            BOOLEAN     DEFAULT 1
             )                 
        ''')
        sql["cursor"].execute('''
            CREATE TABLE IF NOT EXISTS message(
                id INTEGER        PRIMARY     KEY AUTOINCREMENT,
                id_user INTEGER NOT NULL,
                message_id INTEGER NOT NULL,
                message_text TEXT NOT NULL,
                date_send DATE,
                status BOOLEAN DEFAULT 0 CHECK(status IN (0, 1)),
                FOREIGN KEY (id_user) REFERENCES users(id) 
            )                  
        ''')
        self.close(sql["cursor"], sql["connect"])

        return id_message
    
    def check_message
        pass

    def connect_db(self):
        with sqlite3.connect(self.db_name) as connect:
            cursor = connect.cursor()
        return {"connect": connect, "cursor": cursor}
    

    def check_user(self, user_id):
        sql = self.connect_db()
        sql['cursor'].execute('''
            SELECT * FROM users WHERE id_telegram = ?                        
        ''', (user_id, ))

        info_users = sql['cursor'].fetchone()

        self.close(sql['cursor'], sql['connect'])

        if info_users is None:
            return {
                'status' : False
            }
        return {
            'status': True
        }
    def create_user(self, message: dict):


        
        sql = self.connect_db()
        date = datetime.datetime.now().strftime('%Y-%m-%d')

        sql['cursor'].execute('''
            INSERT INTO users (
                id_telegram, username, first_name, last_name, date_reqistration
            )   VALUES (?, ?, ?, ?, ?)
        ''', (
            message.from_user.id,
            message.from_user.username,
            message.from_user.first_name,
            message.from_user.last_name,
            date
        ))
        sql['connect'].commit()
        self.close(sql['cursor'], sql['connect'])
    def insert_message(self, message: dict):
        sql = self.connect_db()
        date = datetime.datetime
        
    def close(self, cursor, connect):
        cursor.close()
        connect.close()
        


class TelegramBot(DataBase):
    def __init__(self, db_name, token):
        super().__init__(db_name)
        self.bot = telebot.TeleBot(token)
        self.router()
        self.admin_chat_id = -1009175397

    def router(self):

        @self.bot.message_handler(commands=['start'])
        def start(message):
            text = ''

            if self.check_user(message.from_user.id)['status']:
                text += 'С возвращением!'
            else:
                self.create_user(message)
                text += f'Добро пожаловать, {message.from_user.first_name}'

            
            self.bot.send_message(
                message.chat.id,
                text
            )

        @self.bot.message_handler(func=lambda message: True)
        def echo_all(message):
            if message.chat.id != self.admin_chat_id:
                self.insert_message(message)
                self.bot.reply_to(
                message,
                "Сообщение отправлено админу!"
            )
            text = f'''
Номер заявки №{id_message}
ID пользователя: {message.from_user.id}
Сообщение: {message.text}

            '''

            self.bot.send_message(self.admin_chat_id, "Новая заявка")
        
        elif message.chat.id == self.admin_chat_id and message.reply_to_message != None:
                reply_message = message.reply_to_message.text
            id_application = re.search(r'Номер заявки №(\d+)', reply_message).group(1)
            id_user = re.search(r'ID пользователя:(\d+)', reply_message).group(1)
                message_text = reply_message.split("\n")[2].split(': ')[-1]
        
            current_text = message_text
        
            self.bot.send_message(
                id_user,
                f'Ответ от админа: {current_text}'
                reply_to_message_id=
            )
            
        
        self.bot.polling()


TelegramBot(
    db_name="tg.db",
    token="6952883016:AAFhj4mM50eKzhNM__5huEdwfs-gg9oyAGg"
)
