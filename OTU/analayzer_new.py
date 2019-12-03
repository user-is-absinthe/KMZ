import os


PATH_TO_FILES = r'/Users/owl/Pycharm/PycharmProjects/KMZ/OTU/files/'
PATH_TO_SAVE_FILES = PATH_TO_FILES  # + 'out/'
PATH_TO_CSV = PATH_TO_SAVE_FILES + r'!_all.csv'
PATH_TO_JSON = PATH_TO_SAVE_FILES + r'!_all.json'

BADLY = 0

try:
    os.makedirs(PATH_TO_SAVE_FILES)
except FileExistsError:
    pass


def main():
    p = PATH_TO_FILES
    files = os.listdir(p)
    # print(worker(r'/Users/owl/Pycharm/PycharmProjects/KMZ/OTU/files/1203145832_46664.ktg'))
    default_keys = ['filename', 'ktg', 'tlg', 'time', 'from', 'to', 'Tmake', 'case', 'ktg_body']
    csv_line_writer(
        path=PATH_TO_CSV,
        data=default_keys,
        separator=';',
        encode='utf-8'
    )
    json_loader = {'filename': [], 'ktg': [], 'tlg': [], 'time': [], 'from': [], 'to': [], 'Tmake': [], 'case': [], 'ktg_body': []}
    for index, file in enumerate(files):
        print('{0}%\t-\t{1}/{2}'.format(round((index + 1) / len(files) * 100), index + 1, len(files)))
        if '.ktg' in file:
            to_file = worker(p + file)
            to_file['filename'] = file
            if to_file == -1:
                continue
            # this
            to_file_l = list()
            for k in ['filename', 'ktg', 'tlg', 'time', 'from', 'to', 'Tmake', 'case', 'ktg_body']:
                json_loader[k].append(to_file[k])
                to_file_l.append(to_file[k])
            csv_line_writer(
                path=PATH_TO_CSV,
                data=to_file_l,
                separator=';',
                encode='utf-8'
            )
    # with open(PATH_TO_JSON, 'w') as file:
    #     json.dump(json_loader, file)
    print(BADLY)
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
    dict_ktg, body = opener(path)
    if dict_ktg == -1:
        return -1
    dict_ktg['case'] = check_case(body)
    dict_ktg['ktg_body'] = body
    return dict_ktg


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


def opener(path_list):
    global BADLY
    try:
        with open(path_list, 'r') as fi:
            file = fi.readlines()
            meta = file[0]
            my_dict = get_meta(meta)
            body = file[1]
        return my_dict, body
    except UnicodeDecodeError:
        BADLY += 1
        meta_data, bin_data = read_data_bin(path_list)
        my_dict, body = get_meta(meta_data), bin_data
        return my_dict, body


def get_meta(text):
    text = text.replace('\n', '').split(';')
    my_dict = dict()
    for key_value in text:
        key_value = key_value.split(':')
        my_dict[key_value[0]] = key_value[1]
    return my_dict


def read_data_bin(fname):
    bin_file = open(fname, "rb").read()
    meta_data = "".join([chr(i) for i in bin_file]).split("\n")[0].strip()
    # bin_data = bin_file[len(meta_data):]
    bin_data = ''
    return meta_data, bin_data


def write_data_bin(fname, meta_data, bin_data):
    with open(fname, "wb") as f:
        f.write(meta_data.encode("ansi") + bin_data)


if __name__ == '__main__':
    main()
