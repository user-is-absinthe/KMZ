PATH_TO_CLOSED = r'/Users/owl/Pycharm/PycharmProjects/KMZ/OTU/files/out/closed/!_meta.tsv'
PATH_TO_OPEN = r'/Users/owl/Pycharm/PycharmProjects/KMZ/OTU/files/out/opened/!_meta.tsv'
PATH_TO_TSV = r'/Users/owl/Pycharm/PycharmProjects/KMZ/OTU/files/out/graph.tsv'


def main():
    closed_data = csv_reader(
        path=PATH_TO_CLOSED, separator='\t', headline=True
    )
    opened_data = csv_reader(
        path=PATH_TO_OPEN, separator='\t', headline=True
    )
    # print(closed_data['from'])
    indexes_get = list()  # (opened_id, closed_id)
    for index, ktg in enumerate(opened_data['ktg']):
        if ktg in closed_data['ktg']:
            indexes_get.append(
                (index, closed_data['ktg'].index(ktg))
            )

    colors = ['red' for i in closed_data['case']]

    replase_names = list()  # (from: (open_name, closed_name), to: (...))
    for changed_index in indexes_get:
        replase_names.append((
            (opened_data['from'][changed_index[0]], closed_data['from'][changed_index[1]]),
            (opened_data['to'][changed_index[0]], closed_data['to'][changed_index[1]])
        ))
    replase_names = list(set(replase_names))

    for change_names in replase_names:
        # (from: (open_name, closed_name), to: (open_name, closed_name))
        # ('Baldr-W', 'a40104'), ('Frigg', 'a40004'))
        indices_from = [i for i, x in enumerate(closed_data['from']) if x == change_names[0][1]]
        # indices_to = [i for i, x in enumerate(closed_data['to']) if x == change_names[1][1]]
        for index in range(len(closed_data['from'])):
            for i_from in indices_from:
                if index == i_from:
                    if change_names[0][0] != closed_data['from'][index]:
                        closed_data['from'][index] = '{0} ({1})'.format(
                            change_names[0][0], change_names[0][1]
                        )
                    if change_names[1][0] != closed_data['to'][index]:
                        closed_data['to'][index] = '{0} ({1})'.format(
                            change_names[1][0], change_names[1][1]
                        )
                    colors[index] = 'green'

        pass

    # print(indexes_get)
    # print(replase_names)
    # print(closed_data['from'])
    # print(closed_data['to'])
    # print(colors)
    # exit_list = [('from', 'to', 'color')]
    csv_line_writer(
        path=PATH_TO_TSV, data=('from', 'to', 'color')
    )
    for index in range(len(closed_data['from'])):
        # exit_list.append((
        #     closed_data['from'][index],
        #     closed_data['to'][index],
        #     colors[index]
        # ))
        csv_line_writer(
            path=PATH_TO_TSV,
            data=(
                closed_data['from'][index],
                closed_data['to'][index],
                colors[index]
            )
        )
    # csv_line_writer(
    #     path=PATH_TO_TSV, data=exit_list
    # )


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


if __name__ == '__main__':
    main()
