TEXT = 'aaa'

LEN_CUT = 2


def list_to_str(lst):
    return_word = ''
    for i in lst:
        return_word += i
    return return_word

if __name__ == '__main__':
    a = TEXT.replace(' ', '')
    index = LEN_CUT
    a = list(a)
    max_len = len(a) * (index + 1) // index + 1
    temp_index = index
    while True:
        a.insert(temp_index, ' ')
        if len(a) >= max_len:
            break
        temp_index += index + 1
    print(list_to_str(a))
