# from bot import save_lin
#
#
#
#
# import os
# import yt_dlp


# url = input(f'Вставьте ссылку для скачивания: {save_lin}')
# print('Качаем!')
# # функция для скачивания видео из YouTube с помощью yt_dlp
# try:
#     def download(url):
#         ydl_opts = {
#             'format': 'mp4'
#             }
#         with yt_dlp.YoutubeDL(ydl_opts) as ydl:
#             ydl.download([url])
#
#     path = 'Videos form YouTube'
#     if path not in os.getcwd():
#         os.chdir(path)
#
#     download(url)
#     print('Файл успешно скачан! Приятного просмотра!')
#
# except Exception:
#     print('Создайте папку <<Videos form YouTube>> для сохранения видео с Youtube и повторите попытку!')