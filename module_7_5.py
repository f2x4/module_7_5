import os
import shutil
import time

from isoduration.formatter import format_time

# print(os.getcwd())
# if os.path.exists('source'):
#     os.chdir('source')
# else:
#     os.mkdir('source')
#     os.chdir('source')
# print(os.getcwd())
# os.chdir(os.pardir)
# print(os.getcwd())
# # os.makedirs(r'source\some_dir\some_subdir')
# # os.makedirs(r'source\some_other_dir\some_other_subdir')
# shutil.copy2(
#     'module_7_4.py', r'source\some_dir\some_subdir\module_7_4.py'
# )
# shutil.copy2(
#     'module_7_3.py', r'source\some_dir\module_7_3.py'
# )
# shutil.copy2(
#     'Walt Whitman - O Captain! My Captain!.txt',
#     r'source\some_other_dir\some_other_subdir\example.txt'
# )

for root, dirs, files in os.walk('source'):
    for dir in dirs:
        path_to_dir = os.path.join(root, dir)
        list_dir = os.listdir(path_to_dir)
        files = [f for f in os.listdir(path_to_dir) if os.path.isfile(f)]
        for file in files:
            # Путь к файлу
            file_path = os.path.join(path_to_dir, file)
            # Время изменения
            file_time = time.ctime(os.path.getatime(file_path))
            # Время создания
            created_time = time.ctime(os.stat(file).st_ctime)
            # Размер файла
            file_size = os.path.getsize(file_path)
            print(
                f'Обнаружен файл: {file},\n'
                f'Путь: {file_path},\n'
                f'Размер: {file_size} байт,\n'
                f'Время создания {created_time},\n'
                f'Время изменения: , {file_time},\n'
                f'Родительская директория: {dir}'
            )


