import collections
import pickle


PATH_TO_CSV = r'/Users/owl/Pycharm/PycharmProjects/KMZ/OTU/files/out/all/!_meta.tsv'
PATH_TO_TEMP = r'/Users/owl/Pycharm/PycharmProjects/KMZ/OTU/files/to_graph/'


def main():
    print(get_big_graph(PATH_TO_CSV))
    print(mini_graph(PATH_TO_CSV, 10))
    pass


def get_big_graph(path_to_tsv):
    data = csv_reader(
        path=path_to_tsv, separator='\t', headline=True
    )
    # print(data.keys())

    from_list = data['from']
    to_list = data['to']
    # print(len(from_list))

    user_list = list(set(from_list + to_list))
    count_send = collections.Counter(zip(from_list, to_list))
    # print(count_send)

    pairs = list()
    for index, _ in enumerate(from_list):
        pairs.append((from_list[index], to_list[index]))
    pairs_bool = list()
    for pair in pairs:
        if (pair[1], pair[0]) in pairs:
            pairs_bool.append(True)
        else:
            pairs_bool.append(False)
    # print(len(pairs_bool), pairs_bool, sep='\n')

    # {id: 3, label: 'Свин'},
    # labels_list = ['{id: {0}, label: \'{1}\'}'.format(index, user) for index, user in enumerate(user_list)]
    # labels = {'id': list(), 'label': list()}
    labels_list = list()
    for index, user in enumerate(user_list):
        # labels_list.append('{id' + ': {0}, label: "{1}"'.format(index + 1, user) + '},')
        # labels['id'].append(index + 1)
        # labels['label'].append(user)
        labels_list.append({'id': index + 1, 'label': user})

    # {from: 1, to: 3, arrows: "to, from", color: 'red'},
    # lines = {'from': list(), 'to': list(), 'arrow': list(), 'color': list(), 'width': list()}
    lines_list = list()
    for index, _ in enumerate(from_list):
        from_user = user_list.index(from_list[index]) + 1
        to_user = user_list.index(to_list[index]) + 1

        if from_user == to_user:
            continue
        # if pairs_bool[index]:
        #     arrow = 'to, from'
        # else:
        #     arrow = 'to'

        arrow = 'to'

        # lines_list.append(
        #     '{' + 'from: {0}, to: {1}, arrows: "{2}", color: "red"'.format(
        #         index + 1, index + 1, arrow
        #     ) + '},'
        # )
        # lines['from'].append(from_user)
        # lines['to'].append(to_user)
        # lines['arrow'].append(arrow)
        # lines['color'].append('green')
        # lines['width'].append(0)

        width = 1
        for cs in count_send.keys():
            if cs[0] == from_list[index] and cs[1] == to_list[index]:
                width = count_send[cs] % 10
                break
            else:
                width = 1
        lines_list.append({
            'from': from_user,
            'to': to_user,
            'arrows': arrow,
            'color': 'green',
            'width': width
        })

    # labels_list = list(set(labels_list))

    # print(labels_list)
    # print(lines_list)
    # print(count_send)
    # print(len(user_list))

    # filename, from, to, time, | status, opened text
    # csv_line_writer(
    #     path=PATH_TO_CSV_TO_ES,
    #     data=['filename', 'from', 'to', 'time', 'status', 'opened_text'],
    # )
    labels_list = dict_checker(labels_list)
    lines_list = dict_checker(lines_list)
    return labels_list, lines_list


def mini_graph(path, id_need):
    labels_list, lines_list = get_big_graph(path_to_tsv=path)
    need_lines = list()
    for line in lines_list:
        if line['from'] == id_need or line['to'] == id_need:
            need_lines.append(line)
    need_cores = list()
    for label in labels_list:
        for line in need_lines:
            if label['id'] == line['from'] or label['id'] == line['to']:
                need_cores.append(label)
    # need_cores = list(set(need_cores))
    # need_lines = list(set(need_lines))
    need_cores = dict_checker(need_cores)
    need_lines = dict_checker(need_lines)
    return need_cores, need_lines


def dict_checker(dict_to_check):
    y, seen = [], []
    for e in dict_to_check:
        if e not in seen:
            y.append(e)
            seen.append(e)
    return y


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


def binary_saver(path, data):
    with open(path, 'wb') as file:
        pickle.dump(data, file)


def binary_opener(path):
    with open(path, 'wb') as file:
        return pickle.load(file)


if __name__ == '__main__':
    main()
