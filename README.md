# telegramBot3

[Ru] Сделаем бота, в котором будут две кнопки: «Факты» и «Поговорки».
Если нажать любую, бот отправит пользователю соответствующее сообщение.

## Требования

* $ pip install -r требования.txt
* создать два файла facts.txt и thinks.txt, которые содержат список интересных фактов и поговорки. ВАЖНО! На каждой строке файлов находится по одному факту или поговорке.
* создать файл config.py, в котором будут храниться токен для доступа к боту в виде
```python
token = "1234567890:ASDFGHH..."
```

## Где взять токен?
* https://xakep.ru/2021/11/28/python-telegram-bots/

## Подключаем модули
```python
import telebot
import random
from telebot import types
from config import token
```

## Примеры использования

#### Загружаем список интересных фактов
```python
f = open('facts.txt', 'r', encoding='UTF-8')
facts = f.read().split('\n')
f.close()
```
#### Загружаем список поговорок
```python
f = open('thinks.txt', 'r', encoding='UTF-8')
thinks = f.read().split('\n')
f.close()
```
#### Если текстовый файл находится не в каталоге программы, то пишем полный путь к нему: "C:/Users/Александр/OneDrive/Рабочий стол/python/FreelanceTask2/freelanceTask3/firstText.txt" (использ.:'/'!)

#### Добавляем две кнопки
```python
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
```
#### Запускаем бота
```python
bot.polling(none_stop=True, interval=0)
```