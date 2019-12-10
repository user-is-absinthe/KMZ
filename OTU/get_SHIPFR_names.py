import os


# C:\Users\user1\Anaconda3>python.exe E:\to_send\get_SHIPFR_names.py
# УГРОЗА - 82
# РЭКС - 80
# ЦИФРЫ-1 - 51
# КАТЯ - 57
PATH_TO_REKS = r"E://to_send//51//"
PATH_TO_OUT = PATH_TO_REKS + '{0}_{1}.chr'
NUMBER = 51

FILE_EXTENSION = r'.ktg'
EXCLUDE = r'BIN.'
IN_NUMBER = ' ' + str(NUMBER)


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
            exit_line += fi[1].replace('.ktg', '') + IN_NUMBER + '\n'
    with open(PATH_TO_OUT.format(counter, NUMBER), 'w') as e_f:
        e_f.write(exit_line)
    pass


if __name__ == '__main__':
    main()