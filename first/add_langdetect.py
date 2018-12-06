import random
import itertools

import langdetect


def list_to_str(lst):
    return_word = ''
    for i in lst:
        return_word += i
    return return_word


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


def replacer(line_list, view=100000):
    to_numerate = len(line_list[0])
    numerate = [hex(j)[2:] for j in range(to_numerate)]
    str_numerate = list_to_str(numerate)
    # line_list.append(str_numerate)
    line_list.insert(0, str_numerate)
    indexes = itertools.permutations([i for i in range(len(line_list[0]))])
    counter = 0
    for permutation in indexes:
        if counter % view == 0:
            now_text = str()
            land_list = list()
            flag = False
            for line in line_list:
                now_line = str()
                for index_letter in range(len(line)):
                    try:
                        # print(line[permutation[index_letter]], end='')
                        now_line += line[permutation[index_letter]]
                    except IndexError:
                        continue
                try:
                    lang_line = langdetect.detect(now_line)
                except langdetect.lang_detect_exception.LangDetectException:
                    lang_line = None
                if lang_line == 'ru':
                    flag = True
                    land_list.append(flag)
                else:
                    land_list.append(flag)
                # print('')
                now_text += now_line + '\n'
            # if flag:
            #     print(now_text)
            #     input('Go next?')
            if land_list.count(True) > land_list.count(False):
                print(now_text)
                input('Go next?')
            # input('\n')
        counter += 1
    pass

if __name__ == '__main__':
    bad_text = 'ЛСКЕК АИЯНИ АДУЛБ МЫАШК ЬАТСА ВЕЛАА НРЧИЛ АУЕЛА ЫШЦМТ ППЗОТ ВЗАТЗ ЕДОИЕ ИПЗДВ ГЗИЕЛ ТЙСЧА ПСПЕХ' + \
           'ЖРОЛД ИЕЕАН ГАРУТ ЮСДУО РЛОУИ ТЦЫНУ ИКОЧО ШЕОДХ РЛАТЛ ЗПООТ АПЧУР МОЕМД ИТСЫЛ ЧАЕАО СТШЙП ОЛПДИ' + \
           'ТСЬАА ИКТАЗ КООТЕ ПЕЫОР ЕГСЛИ НМКОО ПЙПЙР ООНМИ МТМАШ ЛЫИОУ ИУКШХ РЭРЯЕ'
    bad_text = bad_text.replace(' ', '')

    for broken in [10, 11]:
        line_my_len = cut_text(bad_text, broken)
        replacer(line_my_len)
    pass
