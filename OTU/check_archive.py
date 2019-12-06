# Так, к числу наиболее популярных в среде Windows относятся ZIP, RAR, 7z, а в macOS — формат SIT.

import os


PATH_TO_UNKNOWN = r'/Users/owl/Pycharm/PycharmProjects/KMZ/OTU/files/in/'


def main():
    files_list = os.listdir(PATH_TO_UNKNOWN)
    for file in files_list:
        check = check_type(opener(PATH_TO_UNKNOWN + file))
        if check:
            print(file)
    pass


def opener(path):
    with open(path, 'rb') as file:
        return file
    pass


def check_type(archive):
    current_type = archive.read(2)
    if current_type == b'PK':
        return 'zip'
    elif current_type == b'Ra':
        return 'rar'
    elif current_type == b'7z':
        return '7z'
    else:
        return False


if __name__ == '__main__':
    # print(check_type(r'/Users/owl/Pycharm/PycharmProjects/KMZ/OTU/files/test/R2-2.rar'))
    main()
