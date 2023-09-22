import argparse
import os
import tarfile
import zipfile


def extract_filesystem(archive_path):
    """Извлекает файловую систему из архива"""
    if tarfile.is_tarfile(archive_path):
        with tarfile.open(archive_path, 'r') as tar:
            tar.extractall()
    elif zipfile.is_zipfile(archive_path):
        with zipfile.ZipFile(archive_path, 'r') as zip:
            zip.extractall()
    else:
        raise ValueError("Неподдерживаемый формат архива")


def get_current_directory():
    """Возвращает текущую директорию"""
    return os.getcwd()


def list_files(directory):
    """Выводит список файлов и директорий в указанной директории"""
    files = os.listdir(directory)
    for file in files:
        print(file)


def change_directory(directory):
    """Изменяет текущую директорию"""
    os.chdir(directory)


def print_file(file_path):
    """Выводит содержимое файла"""
    with open(file_path, 'r') as file:
        print(file.read())


def main():
    # Парсинг аргументов командной строки
    parser = argparse.ArgumentParser(description='vshell - эмулятор командной строки')
    parser.add_argument('filesystem', help='Путь к файлу с виртуальной файловой системой')
    args = parser.parse_args()

    # Извлечение файловой системы из архива
    extract_filesystem(args.filesystem)

    # Основной цикл эмулятора командной строки
    while True:
        command = input(f'{get_current_directory()} $ ')  # Вывод приглашения командной строки
        command_parts = command.split()

        if command_parts[0] == 'pwd':
            print(get_current_directory())

        elif command_parts[0] == 'ls':
            list_files(get_current_directory())

        elif command_parts[0] == 'cd':
            if len(command_parts) > 1:
                change_directory(command_parts[1])
            else:
                print('Не указана директория')

        elif command_parts[0] == 'cat':
            if len(command_parts) > 1:
                print_file(command_parts[1])
            else:
                print('Не указан файл')

        elif command_parts[0] == 'exit':
            break

        else:
            print('Неподдерживаемая команда')


if __name__ == '__main__':
    main()
