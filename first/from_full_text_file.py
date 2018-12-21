import re
import collections


CLOSED_TEXT = """
ЛСКЕК АИЯНИ АДУЛБ МЫАШК ЬАТСА ВЕЛАА НРЧИЛ АУЕЛА ЫШЦМТ ППЗОТ ВЗАТЗ ЕДОИЕ ИПЗДВ
ГЗИЕЛ ТЙСЧА ПСПЕХ ЖРОЛД ИЕЕАН ГАРУТ ЮСДУО РЛОУИ ТЦЫНУ ИКОЧО ШЕОДХ РЛАТЛ ЗПООТ
АПЧУР МОЕМД ИТСЫЛ ЧАЕАО СТШЙП ОЛПДИ ТСЬАА ИКТАЗ КООТЕ ПЕЫОР ЕГСЛИ НМКОО ПЙПЙР
ООНМИ МТМАШ ЛЫИОУ ИУКШХ РЭРЯЕ
"""
OPEN_TEXT = 'text/Nosov_Vse-Priklyucheniya-Neznayki-v-odnoy-knige.A3hZkQ.380123.fb2'


def is_good_split(closed_text, start=5, stop=15):
    good_split = list()
    for i in range(start, stop):
        tmp_list = text_to_rows(closed_text, i)
        if len(tmp_list[-1]) == len(tmp_list[-2]):
            good_split.append(tmp_list)
    return good_split


def text_to_rows(text, len_row):
    rows_list = list()
    start = 0
    end = len_row
    while True:
        temp_line = text[start:end]
        start = end
        end += len_row
        if temp_line != '':
            rows_list.append(temp_line)
        else:
            break
    return rows_list


def find_str(closed_text, open_text):
    len_now_row = len(closed_text[0])
    start = 0
    end = len_now_row
    answered_list = list()
    for i in range(len(open_text)):
        temp_row = open_text[start:end]
        if collections.Counter(closed_text[0]) == collections.Counter(temp_row):
            answered_list.append((i, temp_row))
        start += 1
        end += 1

    return answered_list


def load_open_text(path=OPEN_TEXT):
    with open(
            path,
            'r') as file:
        full_text = file.read()

    normalazed_text = full_text.replace(' ', '')
    normalazed_text = normalazed_text.replace('.', 'тчк')
    normalazed_text = normalazed_text.replace(',', 'зпт')
    normalazed_text = normalazed_text.replace('\n', '')
    normalazed_text = re.sub(r'[^\w\s]', '', normalazed_text)
    normalazed_text = normalazed_text.upper()
    normalazed_text = normalazed_text.replace('Ё', 'Е')
    normalazed_text = re.sub('<[^<]+>', "", normalazed_text)
    return normalazed_text


def load_closed_text(closed=CLOSED_TEXT):
    closed_text = closed.replace(' ', '')
    closed_text = closed_text.replace('\n', '')
    return closed_text


def my_main():
    # text = load_open_text()
    closed_text = load_closed_text()

    good_splits = is_good_split(closed_text, 8, 13)
    # print(good_splits)

    my_ans = list()
    for variant in good_splits:
        my_ans.append(find_str(variant, closed_text))

    print(my_ans)

    # for splitters in my_ans:
    #     for variant in splitters:
    #         pass

    pass


if __name__ == '__main__':
    my_main()
