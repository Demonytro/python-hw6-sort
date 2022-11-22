# python-hw6-sort - Домашнее задание 6 
# Скрипт должен проходить по указанной во время вызова папке и сортировать все файлы по группам


import os
from pathlib import Path
import sys


name_folders = {
    'images': ('.jpeg', '.png', '.jpg', '.svg'),
    'video': ('.avi', '.mp4', '.mov', '.mkv'),
    'documents': ('.doc', '.docx', '.txt', '.pdf', '.xlsx', '.pptx'),
    'audio': ('.mp3', '.ogg', '.wav', '.amr'),
    'archives': ('.zip', '.gz', '.tar'),
    'unknown': None
}

def normalize(name_files):
    return all


def replace_files(files):


def sort_all(path_folder):

    if path_folder in name_folders:


    list_path_subfolder = path_folder.iterdir()
    if list_path_subfolder == None:
        return
    for file_folder in list_path_subfolder:
        if file_folder.is_dir():
            # subfolder = file_folder.iterdir()
            sort_all(file_folder.iterdir())
            remove dir(file_folder)

        elif file_folder.suffix in name_folders['images']:
            normalize(file_folder)
            replace()

        elif files_folder.suffix in name_folders['video']:
            pass
        elif files_folder.suffix in name_folders['documents']:

        elif files_folder.suffix in name_folders['audio']:

        elif files_folder.suffix in name_folders['archives']:
            разархив
            удалить

        elif files_folder.suffix in name_folders['audio']:

        
        else:
            other





# Скрипт принимает один аргумент при запуске — это имя папки
# path_folders = [] 
# and raise

path_folders = sys.argv[-1]
# print(path_folders)
# D:\GitHub\python-hw6-sort\desktop

for new_folder in name_folders:
    if new_folder.exists():
        raise
    else:
        mkdir(new_folder path_folders)

# all_files = os.listdir(path_folders)
list_path_first = path_folders.iterdir()

for all in list_path_first:
    normalize(all)
    if all in name_folders:
        continue
    if all.is_dir():
        sort_folder
    sort_all(all)

list_sort_done = path_folders.iterdir()
print('Sort done' + list_sort_done)




# 1. Поиск архивов
# 2. Разархив
# 3. создание списка "слепка"
# 3. создание папок
# 3. рекурсия - поиск вложенных папок - сорт - удаление
# 4. Сортировка + переименование

# вы должны вынести логику обработки папки в отдельную функцию
# Чтобы скрипт мог пройти на любую глубину вложенности, функция обработки папок должна рекурсивно вызывать сама себя, когда ей встречаются вложенные папки
# Скрипт должен проходить по указанной во время вызова папке и сортировать все файлы по группам:

#    изображения ('JPEG', 'PNG', 'JPG', 'SVG');
#    видео файлы ('AVI', 'MP4', 'MOV', 'MKV');
#    документы ('DOC', 'DOCX', 'TXT', 'PDF', 'XLSX', 'PPTX');
#    музыка ('MP3', 'OGG', 'WAV', 'AMR');
#    архивы ('ZIP', 'GZ', 'TAR');
#    неизвестные расширения.


# архивы распаковываются и их содержимое переносится в папку archives

# Критерии приёма задания

#     все файлы и папки переименовываются при помощи функции normalize.
#     расширения файлов не изменяются после переименования.
#     пустые папки удаляются
#     скрипт игнорирует папки archives, video, audio, documents, images;
#     распакованное содержимое архива переносится в папку archives в подпапку, названную точно так же, как и архив, но без расширения в конце;
#     файлы, расширения которых неизвестны, остаются без изменений.