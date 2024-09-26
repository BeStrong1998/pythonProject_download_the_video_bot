# import asyncio
# import nest_asyncio
# nest_asyncio.apply()
#
# from aiogram import Bot, Dispatcher, F
# from aiogram.types import FSInputFile
#
# from config import TOKEN
#
# import yt_dlp
# import os
#
#
#
#
# dp = Dispatcher()
# bot = Bot(TOKEN)
#
#
#
# def download_file(url):
#     path = 'Videos form YouTube'
#     if path not in os.getcwd():
#         os.chdir(path)
#     ydl_opts = {
#         'format': 'mp4'
#         }
#     with yt_dlp.YoutubeDL(ydl_opts) as ydl:
#         ydl.download([url])
#
#
# def find_file():
#     files = os.listdir()
#     files.sort(key=os.path.getctime)
#     file = files[-1]
#     new_file = file.replace(' ', '_')
#     os.rename(file, new_file)
#     return new_file
#
#
#
# @dp.message(F.text == '/start')
# async def hendler(message):
#     await message.reply('Введите ссылку на видео')
#
#
# # @dp.message(F.text.contains('youtube'))
# # async def handler(message):
# #     await message.reply('Выполняю скачивание видео')
#
#
# @dp.message(F.text.regexp(r'^https:\/\/(www\.youtube.*|youtu\.be.*|youtube\.com.*)'))
# async def handler(message):
#     download_file(message.tetx)
#     fpath = find_file()
#     file = FSInputFile(fpath)
#     await message.answer_video(file, caption='')
#
# if __name__ == '__main__':
#     loop = asyncio.get_event_loop()
#     loop.create_task(dp.start_polling(bot, skip_updates=True))
#     loop.run_forever()