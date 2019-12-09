import os

PATH_TO_REKS = r'/Users/owl/Pycharm/PycharmProjects/KMZ/OTU/files/examples V/crypto/out/РЕКС'
PATH_TO_OUT = r'/Users/owl/Pycharm/PycharmProjects/KMZ/OTU/files/out/REKS_{0}.chr'
FILE_EXTENSION = r'.ktg'
EXCLUDE = r'BIN.'


if os.name == 'posix':
    DELIMETER = '/'
else:
    DELIMETER = '\\'


def main():
    files_in_dir = os.listdir(PATH_TO_REKS)
    exit_line = str()
    counter = 0
    for index, f in enumerate(files_in_dir):
        if FILE_EXTENSION in f and EXCLUDE not in f:
            print('{0}%\t\t-\t\t{1}/{2}'.format(
                round((index + 1) / len(files_in_dir) * 100), index + 1, len(files_in_dir))
            )
            counter += 1
            fi = f.split('_')
            exit_line += fi[1].replace('.ktg', '') + ' 80' + '\n'
    with open(PATH_TO_OUT.format(counter), 'w') as e_f:
        e_f.write(exit_line)
    pass


if __name__ == '__main__':
    main()
