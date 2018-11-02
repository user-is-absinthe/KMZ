
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

file = open('closed_text.txt', 'r')
closed_text_raw = file.readline().replace('\n', '')
file.close()
print('Len your file-raw {}.'.format(len(closed_text_raw)))

closed_text_raw_list = list(closed_text_raw)
# closed_source_list = []
# for i in closed_text_raw:
#     closed_source_list.append(i)

closed_text = []

for pair in range(len(closed_text_raw_list) / 2):
    closed_text.append(closed_text[pair] + closed_text[pair + 1])

