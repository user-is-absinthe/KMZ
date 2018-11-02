
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
iterator = 0
while True:
    pair = int(closed_text_raw_list[iterator] + closed_text_raw_list[iterator + 1])
    if pair < len(alphabet):
        closed_text.append(pair)
        iterator += 2
    else:
        closed_text.append(int(closed_text_raw_list[iterator]))
        iterator += 1
    if iterator == len(closed_text_raw_list) - 1:
        break
print('Len your closed text is {}.'.format(len(closed_text)))

xz_rand = 0
for move in range(len(alphabet)):
    message = ''
    for letter in closed_text:
        index = letter + move
        if index >= len(alphabet):
            index = index % len(alphabet)
        message += alphabet[index]
        xz_rand += 1
        # print(xz_rand)
    print(message)
    # input('To next?')

