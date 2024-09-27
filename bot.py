import telebot
from config import TOKEN
import os
import yt_dlp



bot = telebot.TeleBot(TOKEN)
dict_links = {}

@bot.message_handler(commands=['start'])
def welcome(message) -> None:
    chat_id = message.chat.id
    mess = f'Введите ссылку на видео\n'
    bot.send_message(chat_id, mess)
    dict_links[chat_id] = {}
    bot.register_next_step_handler(message, save_lin)

def save_lin(message) -> None:
    chat_id = message.chat.id
    link = message.text
    dict_links[chat_id] = link
    bot.send_message(chat_id,
                     f'Отлично, ваша ссылка {link} '
                     f'на видео-файл добавлена в очередь!'
                     f'\nИдёт скачивание видео файла......')
    url = link
    print('Качаем!')
    # функция для скачивания видео из YouTube с помощью yt_dlp
    try:
        def download(url):
            ydl_opts = {
                'merge_output_format': 'mp4',
                'no-playlist': True,
                'playlist_items': '1',
                'format': 'bestvideo[height<=720]+bestaudio/best[height<=720]',
                }
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                ydl.download(url)
        path = 'Video'
        if path not in os.getcwd():
            os.chdir(path)
        download(url)
        print('Файл успешно скачан! Приятного просмотра!')
        bot.send_message(chat_id,
                         f'Загрузка видео-файла завершена, приятного просмотра!')
    except Exception:
        print('Создайте папку <<Video>> для сохранения видео и повторите попытку!')
        bot.send_message(chat_id, 'При попытке скачать видео возникла ошибка!')