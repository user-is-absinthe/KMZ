import itertools

n_text = 'НЫЧОО ИТКЕЕ РТРЗЕ ИУЛТА АССПЧ ЖТТУА КТЗОЗ ТЕТНЭ СВПОА ПВРОЫ НЕВТЗ ДТТКЗ ОИМУЧ ПВАИЗ ИХНИЖ КТМНБ ЫЕЫШЛ АЕЙВН НТЧИТ ЕАОКК ИЕВДГ ЕОТНЬ ОПЧРТ ТИОВТ ЗОЗИИ ЖБВНО НИЫКЧ ЮТБТА ВРЧ'

text = n_text.replace(' ', '')
text = list(text)

len_line = 11
len_colunm = int(len(text) / len_line)

# closed_text = []
# counter = 0
# for i_column in range(len_colunm):
#     closed_text.append([])
#     for i_line in range(len_line):
#         closed_text[0][i_column].append(text[counter])
#         counter += 1
#         pass
#
# print(closed_text)

first_line = text[:11]
more_lines = itertools.permutations(first_line)

count = 0
for i in more_lines:
    print(i)
    count += 1
    if count % 100 == 0:
        input('Now pause.')
