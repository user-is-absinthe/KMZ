import random
import itertools
import difflib
from datetime import datetime


# GLOBAL VARS:
BAD_TEXT = 'ЛСКЕК АИЯНИ АДУЛБ МЫАШК ЬАТСА ВЕЛАА НРЧИЛ АУЕЛА ЫШЦМТ ППЗОТ ВЗАТЗ ЕДОИЕ ИПЗДВ ГЗИЕЛ ТЙСЧА ПСПЕХ' + \
           'ЖРОЛД ИЕЕАН ГАРУТ ЮСДУО РЛОУИ ТЦЫНУ ИКОЧО ШЕОДХ РЛАТЛ ЗПООТ АПЧУР МОЕМД ИТСЫЛ ЧАЕАО СТШЙП ОЛПДИ' + \
           'ТСЬАА ИКТАЗ КООТЕ ПЕЫОР ЕГСЛИ НМКОО ПЙПЙР ООНМИ МТМАШ ЛЫИОУ ИУКШХ РЭРЯЕ'
LEN_LIST = [10, 11]

PATH = '1_0.3.txt'
# open file in win1251

POWER = 0.3
MINIMAL = 4


def list_to_str(lst):
    return_word = ''
    for i in lst:
        return_word += i
    return return_word


def save(text, path=PATH):
    with open(path, 'a') as file:
        file.write(text)
    pass


def random_line(normal_line):
    normal_line = list(normal_line)
    line_to_cut = normal_line.copy()
    len_line = len(normal_line)
    new_line = list()
    for i in range(len_line):
        now_choice = random.choice(line_to_cut)
        new_line.append(now_choice)
        line_to_cut.remove(now_choice)
    return new_line


def cut_text(text, len_line):
    many_lines = list()
    while True:
        temp_line = ''
        try:
            for i in range(len_line):
                temp_line += text[i]
        except IndexError:
            many_lines.append(temp_line)
            break
        many_lines.append(temp_line)
        text = text.replace(temp_line, '')
    return many_lines


def replacer(line_list, view=100000, count_of_point=MINIMAL, polimorph=POWER):
    to_numerate = len(line_list[0])
    numerate = [hex(j)[2:] for j in range(to_numerate)]
    str_numerate = list_to_str(numerate)
    # line_list.append(str_numerate)
    line_list.insert(0, str_numerate)
    indexes = itertools.permutations([i for i in range(len(line_list[0]))])
    counter = 0
    prev = 'z'
    for permutation in indexes:
        if counter % view == 0:
            now_text = str()
            tchk_list = list()
            # flag = False
            for line in line_list:
                now_line = str()
                for index_letter in range(len(line)):
                    try:
                        # print(line[permutation[index_letter]], end='')
                        now_line += line[permutation[index_letter]]
                    except IndexError:
                        continue
                if 'ТЧК' in now_line or 'ЗПТ' in now_line:
                    tchk_list.append(True)
                    now_line += ' <-'
                now_text += now_line + '\n'
            # if flag:
            #     print(now_text)
            #     input('Go next?')
            if len(tchk_list) >= count_of_point:
                # c = 0
                # print(now_text)
                to_difflib = str()
                for index_letter in range(len(line_list[1])):
                    to_difflib += line_list[1][permutation[index_letter]]
                # to_difflib = line_list[1]
                to_if = difflib.SequenceMatcher(a=prev.lower(), b=to_difflib.lower()).ratio()
                if to_if < polimorph:
                    print(now_text)
                    save(now_text)
                    prev = to_difflib

                    now_time = datetime.now()
                    to_write_1 = '[' + now_time.strftime("%B %d %Y, %H:%M:%S") + ']'
                    print('Now time {}.'.format(to_write_1))
                    el_time_1 = now_time - start_time
                    to_write_1 = '[' + str(el_time_1) + ']'
                    print('Before start {}.'.format(to_write_1))
                # input('Go next?')
            # input('\n')
        counter += 1
    pass


if __name__ == '__main__':
    bad_text = BAD_TEXT
    bad_text = bad_text.replace(' ', '')

    start_time = datetime.now()
    to_write = '[' + start_time.strftime("%B %d %Y, %H:%M:%S") + ']'
    print('Start time {}.'.format(to_write))

    for broken in LEN_LIST:
        line_my_len = cut_text(bad_text, broken)
        replacer(line_my_len, 1)

    end_time = datetime.now()
    to_write = '[' + end_time.strftime("%B %d %Y, %H:%M:%S") + ']'
    print('End time {}.'.format(to_write))
    el_time = end_time - start_time
    to_write = '[' + str(el_time) + ']'
    print('Elapsed time {}.'.format(to_write))
