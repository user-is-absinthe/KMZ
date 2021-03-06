import os
import chardet
import binascii
import networkx
import matplotlib.pyplot
import shutil


OPENED = False
# OPENED = True


if OPENED:
    mini_dir = 'opened'
else:
    mini_dir = 'closed'


PATH_TO_FILES = r'/Users/owl/Pycharm/PycharmProjects/KMZ/OTU/files/in/{0}/'.format(mini_dir)
PATH_TO_SAVE_FILES = r'/Users/owl/Pycharm/PycharmProjects/KMZ/OTU/files/out/{0}/'.format(mini_dir)
TO_CHECK = [r'.tlg', r'.']

# PATH_TO_HEX = PATH_TO_SAVE_FILES + r'hex_files/'
PATH_TO_CSV = PATH_TO_SAVE_FILES + r'!_meta.tsv'
PATH_TO_IMG = PATH_TO_SAVE_FILES + r'groups/'
PATH_TO_BAD = PATH_TO_SAVE_FILES + r'unknown/'

BADLY = 0
HEX_DATA = list()
ENCODING = 'utf-16'

CH = [
    PATH_TO_IMG, PATH_TO_BAD
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
    global BADLY, HEX_DATA, TO_CHECK
    p = PATH_TO_FILES
    files = os.listdir(p)
    default_keys = ['filename', 'ktg', 'tlg', 'time', 'from', 'to', 'Tmake', 'case']
    if NEW_LINE:
        save_first_row(path=PATH_TO_CSV, row=default_keys)
    # all_data = list()
    big_graph = networkx.MultiDiGraph()
    for index, file in enumerate(files):
        print('Created big graph: {0}%\t\t-\t\t{1}/{2}'.format(
            round((index + 1) / len(files) * 100), index + 1, len(files)
        ))
        check_flag = False
        for c in TO_CHECK:
            if c in file:
                check_flag = True
        if check_flag:
            to_file, body_file = worker(p + file)
            if to_file == -1:
                # continue
                to_file = {
                              'filename': '', 'ktg': '', 'tlg': '',
                              'time': '', 'from': '', 'to': '', 'Tmake': '', 'case': ''
                }
            to_file['filename'] = file
            # this
            to_file_l = list()
            try:
                for k in default_keys:
                    to_file_l.append(to_file[k])
            except KeyError:
                HEX_DATA.append(p + file)
                # to_file = {
                #     'filename': '', 'ktg': '', 'tlg': '',
                #     'time': '', 'from': '', 'to': '', 'Tmake': '', 'case': to_file['case']
                # }
                continue
            csv_line_writer(
                path=PATH_TO_CSV,
                data=to_file_l,
                separator='\t',
                encode=ENCODING
            )
            # all_data.append(to_file_l)
            # write_data_bin(PATH_TO_HEX + file + '.hex', body_file)
            big_graph.add_edge(to_file_l[4], to_file_l[5])

    networkx.draw(big_graph, with_labels=True)
    matplotlib.pyplot.savefig(PATH_TO_IMG + '!_big_graph.png', format='png')
    matplotlib.pyplot.close()

    weak_connectivity_list = sorted(
        networkx.weakly_connected_components(big_graph),
        key=len, reverse=True
    )
    print('Created minigraphs.')
    minigraph_list = list()
    for user_list in weak_connectivity_list:
        temp_graph = networkx.MultiDiGraph()
        for user in user_list:
            edges_in = big_graph.in_edges(user)
            for edge in edges_in:
                temp_graph.add_edge(edge[0], edge[1])
            edges_out = big_graph.out_edges(user)
            for edge in edges_out:
                temp_graph.add_edge(edge[0], edge[1])
            # print(edges_in)
            # sys.exit(1)

        minigraph_list.append(temp_graph)

    # networkx.draw(big_graph)
    # matplotlib.pyplot.show()

    data_dict = csv_reader(
        path=PATH_TO_CSV, separator='\t',
        headline=True, encode=ENCODING
    )

    for index, t_graph in enumerate(minigraph_list):
        print('Work with minigraphs: {0}%\t\t-\t\t{1}/{2}'.format(
            round((index + 1) / len(minigraph_list) * 100), index + 1, len(minigraph_list)
        ))
        user_list = t_graph.nodes
        lines_list = list()
        for node in user_list:
            try:
                # from_list = data_dict['from'].index(node)
                from_list = [i for i, x in enumerate(data_dict['from']) if x == node]
            except ValueError:
                from_list = []
            try:
                # to_list = data_dict['to'].index(node)
                to_list = [i for i, x in enumerate(data_dict['to']) if x == node]
            except ValueError:
                to_list = []
            lines_list += from_list
            lines_list += to_list
            # print(from_list)
            # print(to_list)

        networkx.draw_shell(t_graph, with_labels=True)
        save_patch = PATH_TO_IMG + str(user_list) + '/'
        check_patch(save_patch)
        matplotlib.pyplot.savefig(save_patch + '!_graph' + '.png', format='png')
        matplotlib.pyplot.close()

        lines_list = list(set(lines_list))
        save_patch_csv = save_patch + '!_meta.tsv'
        save_first_row(path=save_patch_csv, row=default_keys)
        temp_meta = list()
        for index in lines_list:
            shutil.copyfile(
                PATH_TO_FILES + data_dict['filename'][index],
                save_patch + data_dict['filename'][index]
            )
            temp_temp_meta = list()
            for key_i in default_keys:
                temp_temp_meta.append(data_dict[key_i][index])
            temp_meta.append(temp_temp_meta)

        csv_data_writer(path=save_patch_csv, data=temp_meta)

    # print(BADLY)
    # print(HEX_DATA)

    # move badly
    for p in HEX_DATA:
        f_name = p.replace(PATH_TO_FILES, '')
        shutil.copyfile(
            p,
            PATH_TO_BAD + f_name
        )


def save_first_row(path, row):
    csv_line_writer(
        path=path,
        data=row,
        separator='\t',
        encode='utf-16'
    )
    pass


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


def csv_reader(path, separator, headline=False, encode='utf-16'):
    with open(path, 'r', encoding=encode) as file:
        csv_file = file.readlines()
    csv_file = [this[:-1] for this in csv_file]
    if headline:
        keys_to_dict = csv_file[0].split(separator)
    else:
        keys_to_dict = [i for i in range(0, len(csv_file[0].split(separator)))]

    opened_csv = dict()
    for key in keys_to_dict:
        opened_csv[key] = list()

    for line in csv_file:
        if headline and line == csv_file[0]:
            continue
        separated_line = line.split(separator)
        for index in range(len(keys_to_dict)):
            temp_keys_to_dict = keys_to_dict[index]
            temp_separated_line = separated_line[index]
            opened_csv[temp_keys_to_dict].append(temp_separated_line)

    return opened_csv


def worker(path):
    # dict_ktg, body = opener(path)
    dict_ktg, body = read_data_bin(path)
    if dict_ktg == -1:
        return -1, -1
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


def read_data_bin(fname, reusable=False, body=None):
    # print(fname)
    global BADLY, HEX_DATA
    if not reusable and body is not None:
        bin_file = body
    else:
        bin_file = open(fname, "rb").read()
    len_meta_data = len("".join([chr(i) for i in bin_file]).split("\n")[0].strip())
    meta_data_raw = bin_file[0:len_meta_data]
    meta_encode = chardet.detect(meta_data_raw)['encoding']
    # print(chardet.detect(meta_data_raw))
    if chardet.detect(meta_data_raw)['confidence'] < 0.9:
        meta_encode = 'windows-1251'
    try:
        meta_data = meta_data_raw.decode(meta_encode)
    except UnicodeDecodeError:
        meta_data = "".join([chr(i) for i in meta_data_raw])
    # if chardet.detect(meta_data_raw)['encoding'] is None:
    #     # bin_file = binascii.unhexlify(bin_file)
    #     return -1, -1
    try:
        meta_data = get_meta(meta_data)
    except IndexError:
        # print(fname)
        HEX_DATA.append(fname)
        BADLY += 1
        return -1, -1
    bin_data = binascii.hexlify(bin_file[len_meta_data:])

    return meta_data, bin_data


def write_data_bin(fname, data):
    with open(fname, "wb") as f:
        f.write(data)


def csv_data_writer(path, data, separator='\t', encode='utf-16'):
    with open(path, 'a', encoding=encode) as csv_file:
        for line in data:
            now_line = ''
            for index_column in range(len(line)):
                now_line += str(line[index_column])
                if index_column != len(line) - 1:
                    now_line += separator
            now_line += '\n'
            csv_file.write(now_line)
    pass


if __name__ == '__main__':
    main()