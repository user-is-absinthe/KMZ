# Так, к числу наиболее популярных в среде Windows относятся ZIP, RAR, 7z, а в macOS — формат SIT.

import os


PATH_TO_UNKNOWN = r'/Users/owl/Pycharm/PycharmProjects/KMZ/OTU/files/any_examples/'


def main():
    files_list = os.listdir(PATH_TO_UNKNOWN)
    for file in files_list:
        if file != '.DS_Store':
            print(file, end=' ')
            file_body = opener(PATH_TO_UNKNOWN + file)
            check = check_type(file_body)
            if check:
                print(check)
            else:
                print('\n')
    pass


def opener(path):
    with open(path, 'rb') as file:
        return file.read()
    pass


def check_type(file):
    current_type = file[:2]
    # ct = file.read()
    # print(1, ct[len(ct) - 2:])
    # print(2, current_type)
    if current_type == b'PK':
        return 'zip'
    elif current_type == b'Ra':
        return 'rar'
    elif current_type == b'7z':
        return '7z'
    elif current_type == b'RI':
        return 'wav'
    elif current_type == b'\xff\xd8':
        return 'jpg'
    # elif ct[len(ct) - 2:]:
    #     return 'png'
    else:
        print(current_type)
        return False


if __name__ == '__main__':
    # print(check_type(r'/Users/owl/Pycharm/PycharmProjects/KMZ/OTU/files/test/R2-2.rar'))
    main()
