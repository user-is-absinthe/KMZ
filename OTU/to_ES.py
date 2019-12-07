PATH_TO_CSV = r'/Users/owl/Pycharm/PycharmProjects/KMZ/OTU/files/out/!_meta.tsv'
PATH_TO_CSV_TO_ES = r'/Users/owl/Pycharm/PycharmProjects/KMZ/OTU/files/out/!_graph.tsv'


def main():
    data = csv_reader(
        path=PATH_TO_CSV, separator='\t', headline=True
    )
    print(data.keys())

    # filename, from, to, time, | status, opened text
    csv_line_writer(
        path=PATH_TO_CSV_TO_ES,
        data=['filename', 'from', 'to', 'time', 'status', 'opened_text'],
    )

    for index in range(len(data['filename'])):
        if data['from'][index] != '' and data['to'][index] != '':
            save_line = [
                data['filename'][index],
                data['from'][index],
                data['to'][index],
                data['time'][index],
                '',
                ''
            ]
            csv_line_writer(path=PATH_TO_CSV_TO_ES, data=save_line)

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


if __name__ == '__main__':
    main()
