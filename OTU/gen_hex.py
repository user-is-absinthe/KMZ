import os
import chardet
import binascii


PATH_TO_FILES = r'/Users/owl/Pycharm/PycharmProjects/KMZ/OTU/files/in/'
PATH_TO_SAVE_FILES = r'/Users/owl/Pycharm/PycharmProjects/KMZ/OTU/files/out/'

PATH_TO_HEX = PATH_TO_SAVE_FILES + r'hex_files/'
PATH_TO_CSV = PATH_TO_SAVE_FILES + r'!_meta.tsv'
PATH_TO_IMG = PATH_TO_SAVE_FILES + r'graphs/'

CH = [
    PATH_TO_HEX, PATH_TO_IMG
]
for p_i in CH:
    try:
        os.makedirs(p_i)
    except FileExistsError:
        pass

if os.path.exists(PATH_TO_CSV):
    NEW_LINE = False
else:
    NEW_LINE = True


def main():
    p = PATH_TO_FILES
    files = os.listdir(p)
    if NEW_LINE:
        default_keys = ['filename', 'ktg', 'tlg', 'time', 'from', 'to', 'Tmake', 'case']
        csv_line_writer(
            path=PATH_TO_CSV,
            data=default_keys,
            separator='\t',
            encode='utf-16'
        )
    # all_data = list()
    for index, file in enumerate(files):
        print('{0}%\t\t-\t\t{1}/{2}'.format(round((index + 1) / len(files) * 100), index + 1, len(files)))
        if '.ktg' in file:
            to_file, body_file = worker(p + file)
            to_file['filename'] = file
            if to_file == -1:
                continue
            # this
            to_file_l = list()
            for k in ['filename', 'ktg', 'tlg', 'time', 'from', 'to', 'Tmake', 'case']:
                to_file_l.append(to_file[k])
            csv_line_writer(
                path=PATH_TO_CSV,
                data=to_file_l,
                separator='\t',
                encode='utf-16'
            )
            # all_data.append(to_file_l)
            write_data_bin(PATH_TO_HEX + file + '.hex', body_file)


def check_patch(patch_to_check):
    try:
        os.makedirs(patch_to_check)
    except FileExistsError:
        pass


def csv_line_writer(path, data, separator='\t', encode='utf-16'):
    with open(path, 'a', encoding=encode) as csv_file:
        line = ''
        for index_column in range(len(data)):
            line += str(data[index_column])
            if index_column != len(data) - 1:
                line += separator
        line += '\n'
        csv_file.write(line)
    pass


def worker(path):
    # dict_ktg, body = opener(path)
    dict_ktg, body = read_data_bin(path)
    if dict_ktg == -1:
        return -1
    dict_ktg['case'] = check_case(body)
    # dict_ktg['ktg_body'] = body
    return dict_ktg, body


def check_case(text_l):
    alphabet_kate = {
        'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',
        'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p'
    }

    # saver(path=path_l[0], prefix='test', postfix=True)

    if set(text_l) == alphabet_kate:
        # case 1: Kate
        return 'caterine'
        pass
    elif len(set(text_l)) % 12 == 0 and len(set(text_l)) % 8 != 0:
        # case 2: Reks
        return 'reks'
        pass
    elif len(set(text_l)) % 8 == 0 and len(set(text_l)) % 12 != 0:
        # case 3: Magma & Lava
        return 'magma_lava'
        pass
    elif len(text_l) > 1000 and len(set(text_l)) % 256 == 0:
        # case 4: Ugroza
        return 'ugroza'
        pass
    else:
        # other hrenb
        return 'unknown'


def get_meta(text):
    text = text.replace('\n', '').split(';')
    my_dict = dict()
    for key_value in text:
        key_value = key_value.split(':')
        my_dict[key_value[0]] = key_value[1]
    return my_dict


def read_data_bin(fname):
    # print(fname)
    bin_file = open(fname, "rb").read()
    len_meta_data = len("".join([chr(i) for i in bin_file]).split("\n")[0].strip())
    meta_data = bin_file[0:len_meta_data]
    meta_encode = chardet.detect(meta_data)['encoding']
    if chardet.detect(meta_data)['confidence'] < 0.9:
        meta_encode = 'windows-1251'
    # print(meta_encode, chardet.detect(meta_data)['confidence'])
    try:
        meta_data = meta_data.decode(meta_encode)
    except UnicodeDecodeError:
        meta_data = "".join([chr(i) for i in meta_data])
    meta_data = get_meta(meta_data)
    bin_data = binascii.hexlify(bin_file[len_meta_data:])

    return meta_data, bin_data


def write_data_bin(fname, data):
    with open(fname, "wb") as f:
        f.write(data)


if __name__ == '__main__':
    main()
