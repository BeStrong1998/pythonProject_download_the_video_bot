import telebot
import os
import yt_dlp
from telebot.types import InputFile
from config import token


bot = telebot.TeleBot(token)


# @bot.message_handler(commands=['start'])
# def hendler(message):
#     chat_id = message.chat.id
#     bot.send_message(chat_id, f'Привет я бот!'
#                               f'\nОтправь мне ссылку на видео-файл и я его скачаю для тебя')


try:
    # функция для скачивания файла
    def download_video(url):
        path = 'Video'
        if path not in os.getcwd():
            os.chdir(path)
        ydl_opts = {
            'merge_output_format': 'mp4',
            'no-playlist': True,
            'playlist_items': '1',
            'format': 'bestvideo[height<=144]+bestaudio/best[height<=144]',
            }
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
            print('Файл успешно скачан! Приятного просмотра!')
except Exception:
    print('Создайте папку <<Video>> для сохранения видео и повторите попытку!')
    # @bot.message_handler()
    # def errors(message):
    #     chat_id = message.chat.id
    #     bot.send_message(chat_id, f'Ошибка при скачивание видео-файла!')


def find_file():
    files = os.listdir()
    files.sort(key=os.path.getctime)
    file = files[-1]
    new_file = file.replace(' ', '_')
    os.rename(file, new_file)
    return new_file


@bot.message_handler()
def welcome(message) -> None:
    # chat_id = message.chat.id
    # bot.send_message(chat_id, f'Отлично, теперь твоя ссылка добавлена в очередь!')
    # bot.send_message(chat_id, f'Идёт процесс скачивания видео-файла......')
    download_video(message.text)
    fpath = find_file()
    file = InputFile(fpath)
    chat_id = message.chat.id
    bot.send_video(chat_id, file)
    bot.send_message(chat_id,
                     f'Загрузка видео-файла завершена, приятного просмотра!')

