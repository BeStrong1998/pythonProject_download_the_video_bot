# import os
#
#
# def find_file():
#     files = os.listdir()
#     files.sort(key=os.path.getctime)
#     file = files[-1]
#     new_file = file.replace(' ', '_')
#     os.rename(file, new_file)
#     return new_file