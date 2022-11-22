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


def replace_files(files):


def sort_files(folder):
    for files_folder in folder:
        if files.is_dir():
            sort_files(files_folder)
            remove dir(files_folder)

        elif files_folder.suffix in name_folders['images']:

        elif files_folder.suffix in name_folders['video']:

        elif files_folder.suffix in name_folders['documents']:

        elif files_folder.suffix in name_folders['audio']:

        elif files_folder.suffix in name_folders['archives']:

        elif files_folder.suffix in name_folders['audio']:

        
        else:
            other





# Скрипт принимает один аргумент при запуске — это имя папки
# path_folders = [] 
# and raise

path_folders = sys.argv[-1]
# print(path_folders)
# D:\GitHub\python-hw6-sort\desktop

# all_files = os.listdir(path_folders)
list_path_folders = path_folders.iterdir()

sort_files(list_path_folders)

mkdir



# 1. Поиск архивов
# 2. Разархив
# 3. создание списка "слепка"
# 3. создание папок
# 3. рекурсия - поиск вложенных папок - сорт - удаление
# 4. Сортировка + переименование

p.suffix

for count in list_path_folders:
    if path_count.is_dir():
        count_files(path_count)
    else:
        for file in path_count:

    count_files(count)

# вы должны вынести логику обработки папки в отдельную функцию
# Чтобы скрипт мог пройти на любую глубину вложенности, функция обработки папок должна рекурсивно вызывать сама себя, когда ей встречаются вложенные папки
# Скрипт должен проходить по указанной во время вызова папке и сортировать все файлы по группам:

#    изображения ('JPEG', 'PNG', 'JPG', 'SVG');
#    видео файлы ('AVI', 'MP4', 'MOV', 'MKV');
#    документы ('DOC', 'DOCX', 'TXT', 'PDF', 'XLSX', 'PPTX');
#    музыка ('MP3', 'OGG', 'WAV', 'AMR');
#    архивы ('ZIP', 'GZ', 'TAR');
#    неизвестные расширения.

p.exists()

def count_files(path_count):

    


# архивы распаковываются и их содержимое переносится в папку archives

# Критерии приёма задания

#     все файлы и папки переименовываются при помощи функции normalize.
#     расширения файлов не изменяются после переименования.
#     пустые папки удаляются
#     скрипт игнорирует папки archives, video, audio, documents, images;
#     распакованное содержимое архива переносится в папку archives в подпапку, названную точно так же, как и архив, но без расширения в конце;
#     файлы, расширения которых неизвестны, остаются без изменений.