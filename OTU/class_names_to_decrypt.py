from collections import Counter


PATH_TO_CSV = r'/Users/owl/Pycharm/PycharmProjects/KMZ/OTU/files/out/file_classes.tsv'
PATH_TO_EXIT = r'/Users/owl/Pycharm/PycharmProjects/KMZ/OTU/files/out/to_server.chr'


CAN_DECRYPT = {
    'caterine': 57,
    'reks': 80,
}


def main(path_to_csv, path_to_exit_file):
    data = csv_reader(
        path=path_to_csv,
        separator='\t',
        encode='utf-8'
    )
    print(Counter(data[1]))
    exit_list = list()
    for index in range(len(data[0])):
        to_check = list(CAN_DECRYPT.keys())
        if data[1][index] in to_check:
            exit_list.append('{0} {1}'.format(
                data[0][index], CAN_DECRYPT[data[1][index]]
            ))
        pass
    with open(path_to_exit_file, 'w') as file:
        for l in exit_list:
            file.write(l.replace('.ktg', '') + '\r\n')


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
    main(
        path_to_csv=PATH_TO_CSV,
        path_to_exit_file=PATH_TO_EXIT
    )
