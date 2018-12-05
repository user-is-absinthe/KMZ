import random
import itertools


def list_to_str(lst):
    return_word = ''
    for i in lst:
        return_word += i
    return return_word


def random_line(nornal_line):
    nornal_line = list(nornal_line)
    line_to_cut = nornal_line.copy()
    len_line = len(nornal_line)
    new_line = list()
    for i in range(len_line):
        now_choise = random.choice(line_to_cut)
        new_line.append(now_choise)
        line_to_cut.remove(now_choise)
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
    numerate = [hex(i)[2:] for i in range(to_numerate)]
    str_numerate = list_to_str(numerate)
    #line_list.append(str_numerate)
    line_list.insert(0, str_numerate)
    indexes = itertools.permutations([i for i in range(len(line_list[0]))])
    counter = 0
    for permutation in indexes:
        if counter % view == 0:
            for line in line_list:
                for index_letter in range(len(line)):
                    try:
                        print(line[permutation[index_letter]], end='')
                    except IndexError:
                        continue
                print('')
            input('\n')
        counter += 1
    pass


text = 'ЛСКЕК АИЯНИ АДУЛБ МЫАШК ЬАТСА ВЕЛАА НРЧИЛ АУЕЛА ЫШЦМТ ППЗОТ ВЗАТЗ ЕДОИЕ ИПЗДВ ГЗИЕЛ ТЙСЧА ПСПЕХ ЖРОЛД ИЕЕАН ГАРУТ ЮСДУО РЛОУИ ТЦЫНУ ИКОЧО ШЕОДХ РЛАТЛ ЗПООТ АПЧУР МОЕМД ИТСЫЛ ЧАЕАО СТШЙП ОЛПДИ ТСЬАА ИКТАЗ КООТЕ ПЕЫОР ЕГСЛИ НМКОО ПЙПЙР ООНМИ МТМАШ ЛЫИОУ ИУКШХ РЭРЯЕ'
#text = 'НЫЧОО ИТКЕЕ РТРЗЕ ИУЛТА АССПЧ ЖТТУА КТЗОЗ ТЕТНЭ СВПОА ПВРОЫ НЕВТЗ ДТТКЗ ОИМУЧ ПВАИЗ ИХНИЖ КТМНБ ЫЕЫШЛ АЕЙВН НТЧИТ ЕАОКК ИЕВДГ ЕОТНЬ ОПЧРТ ТИОВТ ЗОЗИИ ЖБВНО НИЫКЧ ЮТБТА ВРЧ'
text = text.replace(' ', '')
#text = list(text)
#line = text[:11]
#print(text)

line_my_len = cut_text(text, 11)

#for line in line_my_len:
#	print(line)

# print(random_line(line))

#for i in range(1000):
#	my_line = random_line(line)
#	print(my_line)

replacer(line_my_len)

