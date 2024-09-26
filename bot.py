import telebot
from config import TOKEN
from orm import Links

import os
import yt_dlp

bot = telebot.TeleBot(TOKEN)
ls_links = {}


@bot.message_handler(commands=['start'])
def welcome(message) -> None:
    chat_id = message.chat.id
    mess = (f'Добро пожаловать в бота! '
            f'Введите ссылку')
    bot.send_message(chat_id, mess)
    ls_links[chat_id] = {}
    bot.register_next_step_handler(message, save_lin)

def save_lin(message) -> None:
    chat_id = message.chat.id
    link = message.text
    ls_links[chat_id] = link
    bot.send_message(chat_id,
                     f'Отлично, ваша ссылка добавлена, {link}')



    l = Links(lin=link)
    l.save()
    bot.send_message(chat_id, f'Запись в БД прошла успешно!')
    # for i in Links:
    #     print(i.lin)


    # url = input(f'Вставьте ссылку для скачивания: {link}')
    url = link
    print('Качаем!')
    # функция для скачивания видео из YouTube с помощью yt_dlp
    try:
        def download(url):
            ydl_opts = {
                'format': 'mp4'
                }
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                ydl.download(link)

        path = 'Videos form YouTube'
        if path not in os.getcwd():
            os.chdir(path)

        download(url)
        print('Файл успешно скачан! Приятного просмотра!')

    except Exception:
        print('Создайте папку <<Videos form YouTube>> для сохранения видео с Youtube и повторите попытку!')