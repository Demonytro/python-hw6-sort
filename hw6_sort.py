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

def normalize(path_file):
    # name_files = path_file.name
    # norma_nametranslite
    # rename old_name norma_name


def sort_folder(path_folder):

    list_path_subfolder = path_folder.iterdir()
    if not list_path_subfolder:
        os.rmdir(path_folder)
        return
    else:
        for file_folder in list_path_subfolder:
            if file_folder.is_dir():
                sort_folder(file_folder)
                os.rmdir(path_folder)
            else:
                sort_files(file_folder)


def sort_files(path_file):
    
    if path_file.suffix in name_folders['images']:
        # Path("path/to/current/file.foo").rename("path/to/new/destination/for/file.foo")   
        new_path_name = os.path.join(path_start_folder, 'images', path_file.name)
        
    elif path_file.suffix in name_folders['video']:
        new_path_name = os.path.join(path_start_folder, 'video', path_file.name)

    elif path_file.suffix in name_folders['documents']:
        new_path_name = os.path.join(path_start_folder, 'documents', path_file.name)

    elif path_file.suffix in name_folders['audio']:
        new_path_name = os.path.join(path_start_folder, 'audio', path_file.name)

    elif path_file.suffix in name_folders['audio']:
        new_path_name = os.path.join(path_start_folder, 'audio', path_file.name)

    elif path_file.suffix in name_folders['archives']:
        # разархив
        # удалить or delete
        
        # else:
        #     other
    else:
        # replace(other)
        new_path_name = os.path.join(path_start_folder, 'unknown', path_file.name)

    Path(path_file).rename(new_path_name)
    normalize(new_path_name)
    
    # return





# Скрипт принимает один аргумент при запуске — это имя папки
# path_folders = [] 
# and raise

path_start_folder = sys.argv[-1]
# print(path_folders)
# D:\GitHub\python-hw6-sort\desktop

for new_folder in name_folders:
    path_new_dir = os.path.join(path_start_folder, new_folder)
    try:
        os.mkdir(path_new_dir)
        print('Create new dir ' + path_new_dir)
    except OSError as error:
        print(error)
        raise

# all_files = os.listdir(path_folders)
list_path_first = path_folders.iterdir()

for first_all in list_path_first:
    if first_all in name_folders:
        continue
    if first_all.is_dir():
        sort_folder(first_all)
    else:
        sort_files(first_all)

list_sort_done = path_start_folder.iterdir()
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