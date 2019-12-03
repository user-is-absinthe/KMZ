import os
import collections


if os.name == 'posix':
    DELIMETER = '/'
else:
    DELIMETER = '\\'


def main():
    #####
    path_l = [
        r'/Users/owl/Pycharm/PycharmProjects/KMZ/OTU/files/18599.ktg',
        r'/Users/owl/Pycharm/PycharmProjects/KMZ/OTU/files/18600.ktg',
        r'/Users/owl/Pycharm/PycharmProjects/KMZ/OTU/files/18601.ktg',
        r'/Users/owl/Pycharm/PycharmProjects/KMZ/OTU/files/18602.ktg',
        r'/Users/owl/Pycharm/PycharmProjects/KMZ/OTU/files/18603.ktg'
    ]
    path = path_l[0]
    text_l = opener(path)
    ###
    alphabet_kate = {
        'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',
        'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p'
    }

    # saver(path=path_l[0], prefix='test', postfix=True)

    if set(text_l) == alphabet_kate:
        # case 1: Kate
        saver(path=path, body=text_l, prefix='caterine')
        pass
    elif len(set(text_l)) % 12 == 0 and len(set(text_l)) % 8 != 0:
        # case 2: Reks
        saver(path=path, body=text_l, prefix='reks')
        pass
    elif len(set(text_l)) % 8 == 0 and len(set(text_l)) % 12 != 0:
        # case 3: Magma & Lava
        saver(path=path, body=text_l, prefix='magma_lava')
        pass
    elif len(text_l) > 1000 and len(set(text_l)) % 256 == 0:
        # case 4: Ugroza
        saver(path=path, body=text_l, prefix='ugroza')
        pass
    else:
        # other hrenb
        saver(path=path, body=text_l, prefix='unknown')
        count_2_gram = count_gram(text_l, 2)
        if len(count_2_gram) <= 100:
            exit_line = str(count_2_gram[0][1]) + ': '
            temp = count_2_gram[0][1]
            for i in count_2_gram:
                if i[1] == temp:
                    exit_line += str(i[0]) + '; '
                else:
                    exit_line += '\n' + str(i[0]) + '; '
            saver(path=path, body=text_l, prefix='unknown', postfix=True)
        pass
    pass


def opener(path_list):
    with open(path_list, 'r') as fi:
        body = fi.readlines()
        a = str()
        for line in body:
            a += line.lower()
    return a


def saver(path, body, prefix, postfix=False):
    splited_path = path.split(DELIMETER)
    splited_path[-1] = '[' + prefix + '] ' + splited_path[-1]
    if postfix:
        last = splited_path[-1].split('.')
        splited_path[-1] = last[0] + '.sus'
    new_path = str()
    for i in splited_path:
        new_path += DELIMETER + i
    # print(new_path)
    with open(new_path, 'w') as file:
        file.write(body)


def sort_second(val):
    return val[1]


def count_gram(text, len_gram):
    gram_list = list()
    index_1 = 0
    index_2 = len_gram
    while True:
        temp = text[index_1:index_2]
        index_1 += len_gram
        index_2 += len_gram
        if temp == '':
            break
        else:
            gram_list.append(temp)

    gram_count = collections.Counter(gram_list)

    gram_count_list = list()
    for i in gram_count.keys():
        gram_count_list.append((i, gram_count[i]))
    gram_count_list.sort(key=sort_second, reverse=True)
    return gram_count_list


if __name__ == '__main__':
    main()
