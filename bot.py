import telebot
import os
import yt_dlp
from telebot.types import InputFile
from config import token


bot = telebot.TeleBot(token)



# функция для скачивания файла
def download_video(url):
    print('Идёт процесс скачивания.....')
    path = 'Video'
    if path not in os.getcwd():
        os.chdir(path)
    ydl_opts = {
        'format': 'bestvideo[height<=240]+bestaudio/best[height<=240]',
        'quiet': True,
        'no_warnings': True,
        'outtmpl': '%(id)s.%(ext)s',
        'merge_output_format': 'mp4'
        # 'merge_output_format': 'mp4',
        # 'no-playlist': True,
        # 'playlist_items': '1',
        # 'format': 'bestvideo[height<=144]+bestaudio/best[height<=144]',
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
        print(f'Видео-файл {url} успешно скачен!')


def find_file():
    files = os.listdir()
    files.sort(key=os.path.getctime)
    file = files[-1]
    new_file = file.replace(' ', '_')
    os.rename(file, new_file)
    return new_file


@bot.message_handler()
def handler(message) -> None:
    chat_id = message.chat.id
    download_video(message.text)
    fpath = find_file()
    file = InputFile(fpath)
    bot.send_video(chat_id, file)