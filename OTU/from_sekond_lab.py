import collections


# [
# 'А', 'Б', 'В', 'Г', 'Д', 'Е', 'Ё', 'Ж',
# 'З', 'И', 'Й', 'К', 'Л', 'М', 'Н', 'О',
# 'П', 'Р', 'С', 'Т', 'У', 'Ф', 'Х', 'Ц',
# 'Ч', 'Ш', 'Щ', 'Ъ', 'Ы', 'Ь', 'Э', 'Ю',
# 'Я'
# ]


alphabet = [
    'А', 'Б', 'В', 'Г', 'Д', 'Е', 'Ж', 'З',
    'И', 'Й', 'К', 'Л', 'М', 'Н', 'О', 'П',
    'Р', 'С', 'Т', 'У', 'Ф', 'Х', 'Ц', 'Ч',
    'Ш', 'Щ', 'Ъ', 'Ы', 'Ь', 'Э', 'Ю', 'Я'
]

file = open('/Users/owl/Pycharm/PycharmProjects/KMZ/OTU/files/18599.ktg', 'r')
closed_text_raw = file.readline().replace('\n', '')
file.close()
print('Len your file-raw {}.'.format(len(closed_text_raw)))

closed_text_raw_list = list(closed_text_raw)
# closed_source_list = []
# for i in closed_text_raw:
#     closed_source_list.append(i)

closed_text = []

list_pair = list(zip(closed_text_raw_list[::2], closed_text_raw_list[1::2]))

for i in range(len(list_pair)):
    closed_text.append(int(list_pair[i][0] + list_pair[i][1]))

set_closed_text = list(set(closed_text))

equally_dict = collections.Counter(closed_text)
# Counter(
#   {
#       87: 58, 55: 40, 23: 39, 68: 39, 50: 30, 21: 30,
#       60: 26, 98: 22, 56: 17, 17: 16, 62: 15, 24: 14,
#       44: 14, 97: 14, 48: 12, 88: 12, 85: 11, 31: 8,
#       74: 8, 51: 7, 82: 6, 40: 6, 41: 5, 29: 5, 80: 4,
#       84: 4, 20: 3, 65: 2, 58: 1, 49: 1
#   }
# )
#

number = 85
letter = 'ы'
for i in range(len(closed_text)):
    if number == closed_text[i]:
        closed_text[i] = letter

open_text = ''
for i in closed_text:
    open_text += str(i)

# bi-grams
list_bigramm = []
iteration = 0
# list_bigramm = list(zip(closed_text[::2], closed_text[1::2]))
# equally_2dict = collections.Counter(list_bigramm)
# (68, 87): 8, (68, 55): 6, (87, 50): 5, (87, 98): 4, (55, 50): 4,
# (98, 60): 4, (62, 87): 4, (87, 60): 4, (68, 23): 4, (88, 87): 4,
# (50, 23): 3, (50, 55): 3, (60, 87): 3, (60, 55): 3, (44, 21): 3...
while True:
    list_bigramm.append((closed_text[iteration], closed_text[iteration + 1]))
    if iteration == len(closed_text) - 2:
        break
    iteration += 1
equally_2dict = collections.Counter(list_bigramm)
# (68, 87): 10, (68, 55): 9, (68, 23): 7, (87, 50): 7, (87, 98): 6, (55, 50): 6,
# (23, 23): 6, (98, 60): 6, (50, 55): 6, (62, 87): 6, (50, 23): 5, (23, 50): 5,
# (21, 98): 5, (50, 87): 5, (60, 87): 5, (55, 60): 5, (87, 68): 5, (87, 56): 5,
# (23, 68): 5, (56, 87): 5, (44, 21): 5, (88, 87): 5, (50, 82): 4, (87, 85): 4...



# 3-grams
# list_treegramm = list(zip(closed_text[::2], closed_text[1::2], closed_text[2::3]))
# equally_3dict = collections.Counter(list_treegramm)
# (87, 98, 50): 2, (21, 17, 23): 2, (87, 60, 87): 2, (23, 56, 50): 2, (50, 21, 21): 2,
# (50, 23, 21): 1, (62, 21, 50): 1, (60, 23, 87): 1, (50, 82, 50): 1, (68, 87, 17): 1,
# (85, 23, 55): 1, (50, 24, 68): 1...
list_treegramm = []
iteration = 0
while True:
    list_treegramm.append((closed_text[iteration], closed_text[iteration + 1], closed_text[iteration + 2]))
    if iteration == len(closed_text) - 3:
        break
    iteration += 1
equally_3dict = collections.Counter(list_treegramm)
# (87, 50, 87): 3, (68, 24, 44): 3, (68, 55, 51): 3, (50, 82, 68): 2, (87, 85, 23): 2,
# (50, 48, 85): 2, (87, 44, 68): 2, (44, 68, 55): 2, (21, 68, 23): 2, (56, 55, 50): 2,
# (24, 98, 87): 2, (21, 98, 60): 2, (48, 23, 23): 2, (85, 24, 50): 2, (62, 87, 41): 2,
# (68, 55, 74): 2, (98, 60, 87): 2, (55, 60, 21): 2, (17, 97, 55): 2, (97, 55, 98): 2...



