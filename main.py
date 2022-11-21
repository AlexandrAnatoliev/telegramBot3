# telegramBot3

# Сделаем бота, в котором будут две кнопки: «Факты» и «Поговорки».
# Если нажать любую, бот отправит пользователю соответствующее сообщение.

import telebot
import random
from telebot import types
from config import token

# Загружаем список интересных фактов
#
f = open('facts.txt', 'r', encoding='UTF-8')
facts = f.read().split('\n')
f.close()

# Загружаем список поговорок
f = open('thinks.txt', 'r', encoding='UTF-8')
thinks = f.read().split('\n')
f.close()

# Создаем бота
bot = telebot.TeleBot(token)


# Команда start
@bot.message_handler(commands=["start"])
def start(m, res=False):
    # Добавляем две кнопки
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("Факт")
    item2 = types.KeyboardButton("Поговорка")
    markup.add(item1)
    markup.add(item2)
    bot.send_message(m.chat.id,
                     'Нажми: \nФакт для получения интересного факта\nПоговорка — для получения мудрой цитаты ',
                     reply_markup=markup)


# Получение сообщений от юзера
@bot.message_handler(content_types=["text"])
def handle_text(message):
    # Если юзер прислал 1, выдаем ему случайный факт
    if message.text.strip() == 'Факт':
        answer = random.choice(facts)
    # Если юзер прислал 2, выдаем умную мысль
    elif message.text.strip() == 'Поговорка':
        answer = random.choice(thinks)
    # Отсылаем юзеру сообщение в его чат
    bot.send_message(message.chat.id, answer)


# Запускаем бота
bot.polling(none_stop=True, interval=0)
