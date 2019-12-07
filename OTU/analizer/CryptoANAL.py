import os
import chardet
import binascii
import shutil
import numpy as np
import re
from subprocess import run
#
import matplotlib.pyplot as plt
from matplotlib.ticker import NullFormatter
#
import scipy.stats as stats


PATH_TO_FILES = r'D:\Programming\NomeroffNET\examples\crypto/in/'
PATH_TO_SAVE_FILES = r'D:\Programming\NomeroffNET\examples\crypto/out/'
PATH_TO_RACKS_EXE = r'C:\Users\компьютер\Desktop\Криптограммы_критерии\РЕКС\Проект3\Release\RAKCS.exe'

PATH_TO_TMP_FNAME = r'~temporary.file'

# PATH_TO_HEX = PATH_TO_SAVE_FILES + r'hex_files/'
PATH_TO_CSV = PATH_TO_SAVE_FILES + r'!Метаданные.tsv'
PATH_TO_IMG = PATH_TO_SAVE_FILES + r'Разбиение по источникам/'
PATH_TO_BAD = PATH_TO_SAVE_FILES + r'Без заголовка/'
PATH_TO_BIN = PATH_TO_SAVE_FILES + r'BIN данные/'

PATH_TO_CATERINE     = PATH_TO_SAVE_FILES + r'Катерина/'
PATH_TO_RSA          = PATH_TO_SAVE_FILES + r'RSA/'
PATH_TO_STB1         = PATH_TO_SAVE_FILES + r'STB1/'
PATH_TO_SUBSTITUTION = PATH_TO_SAVE_FILES + r'Подстановка/'
PATH_TO_SIMPLE_REPL  = PATH_TO_SAVE_FILES + r'Простая замена/'
PATH_TO_REKS         = PATH_TO_SAVE_FILES + r'РЕКС/'
PATH_TO_UGROZA       = PATH_TO_SAVE_FILES + r'Угроза НАТО/'
PATH_TO_CITADEL      = PATH_TO_SAVE_FILES + r'Цитадель/'
PATH_TO_OTHER        = PATH_TO_SAVE_FILES + r'Другие шифры/'
PATH_TO_CITADEL_CATERINE = PATH_TO_SAVE_FILES + r'Цитадель или Катерина/'

BADLY = 0
HEX_DATA = list()
ENCODING = 'utf-16'

CH = [
    PATH_TO_IMG,
    PATH_TO_BAD,
    PATH_TO_BIN,

    PATH_TO_CATERINE,
    PATH_TO_RSA,
    PATH_TO_STB1,
    PATH_TO_SUBSTITUTION,
    PATH_TO_SIMPLE_REPL,
    PATH_TO_REKS,
    PATH_TO_UGROZA,
    PATH_TO_CITADEL,
    PATH_TO_OTHER,
    PATH_TO_CITADEL_CATERINE,
]
for p_i in CH:
    try:
        os.makedirs(p_i)
    except FileExistsError:
        pass

if os.path.exists(PATH_TO_CSV):
    NEW_LINE = False
else:
    NEW_LINE = True
    
def check_patch(patch_to_check):
    try:
        os.makedirs(patch_to_check)
    except FileExistsError:
        pass

def get_meta(text):
    text = text.replace('\n', '').split(';')
    my_dict = dict()
    for key_value in text:
        key_value = key_value.split(':')
        my_dict[key_value[0]] = key_value[1]
    return my_dict
    
    
def read_data_bin(fname, reusable=False, body=None):
    # print(fname)
    global BADLY, HEX_DATA
    if not reusable and body is not None:
        bin_file = body
    else:
        bin_file = open(fname, "rb").read()
    len_meta_data = len("".join([chr(i) for i in bin_file]).split("\n")[0].strip())
    meta_data_raw = bin_file[0:len_meta_data]
    meta_encode = chardet.detect(meta_data_raw)['encoding']
    #print(chardet.detect(meta_data_raw))
    if chardet.detect(meta_data_raw)['confidence'] < 0.9:
        meta_encode = 'windows-1251'
    try:
        meta_data = meta_data_raw.decode(meta_encode)
    except UnicodeDecodeError:
        meta_data = "".join([chr(i) for i in meta_data_raw])
    # if chardet.detect(meta_data_raw)['encoding'] is None:
    #     # bin_file = binascii.unhexlify(bin_file)
    #     return -1, -1
    start_pos = len_meta_data
    while start_pos < len(bin_file) and chr(bin_file[start_pos]) in ('\n', '\r'):
        start_pos += 1
    bin_data = bin_file[start_pos:]
    hex_data = hex_strip(str(binascii.hexlify(bin_data)).strip("b'"))
    hex_symbols_data = np.array([int(x, 16) for x in re.findall(r'..', hex_data)])
    try:
        if "ktg" in meta_data:
            meta_data = get_meta(meta_data)
        else: 
            return None, bin_data, hex_data, hex_symbols_data
    except IndexError:
        #print(fname)
        HEX_DATA.append(fname)
        BADLY += 1
        return None, None, None, None
    return meta_data, bin_data, hex_data, hex_symbols_data

    
def hex_strip(hex_string):
    return hex_string[4:] if hex_string.startswith("0d0a") else hex_string

def REKS_decryptor(bin_data):
    open(PATH_TO_TMP_FNAME, "wb").write(bin_data)
    return(run([PATH_TO_RACKS_EXE, PATH_TO_TMP_FNAME]).returncode)

def crypto_classifier(cryptogramm_header, cryptogramm_binary, cryptogramm_hexsym):
#     PATH_TO_CATERINE,
#     PATH_TO_RSA,
#     PATH_TO_STB1,
#     PATH_TO_SUBSTITUTION,
#     PATH_TO_SIMPLE_REPL,
#     PATH_TO_REKS,
#     PATH_TO_UGROZA,
#     PATH_TO_CITADEL,
#     PATH_TO_OTHER,
    if  cryptogramm_header:
        kate_bool = ((ord("A") <= cryptogramm_hexsym) & (cryptogramm_hexsym <= ord("P"))).all()
        citadel_bool = ((ord("A") <= cryptogramm_hexsym) & (cryptogramm_hexsym <= ord("L"))\
                        | (ord("N") == cryptogramm_hexsym)\
                        | (ord("X") == cryptogramm_hexsym)\
                        | (ord("Y") == cryptogramm_hexsym)\
                        | (ord("Z") == cryptogramm_hexsym)).all()
        if kate_bool and citadel_bool:
            # Citadel and caterine
            return PATH_TO_CITADEL_CATERINE, 'citadel_caterine'  
        if citadel_bool:
            # Citadel
            return PATH_TO_CITADEL, 'citadel'
        if kate_bool:
            # Kate
            return PATH_TO_CATERINE, 'caterine'
        text_bin = str(cryptogramm_binary)
        if "key" in text_bin:
            # RSA
            tmp = "".join([chr(i) for i in cryptogramm_binary]).split("Stop public key")[0]
            keys_header = cryptogramm_binary[:len(tmp.strip())].decode("utf-8")
            data = cryptogramm_binary[len(tmp) + len("Stop public key"):]
            
            return PATH_TO_RSA, 'RSA', data, list(map(
                lambda x: x.strip("\n\r "),
                keys_header
                .replace("Start key", "")
                .replace("Stop key", "\n")
                .replace("Start public key", "")
                .split("\n")))
        
        if REKS_decryptor(cryptogramm_binary) == 0:
            return PATH_TO_REKS, 'reks'
        return PATH_TO_OTHER, 'unknown'
    return PATH_TO_BAD, 'file without header'


def classify(fname):
    if '.ktg' not in fname:
        return PATH_TO_UNKNOWN
        
    cryptogramm_headers, cryptogramm_binary, \
    cryptogramm_hexbin, cryptogramm_hexsymb = read_data_bin(os.path.join(PATH_TO_FILES, file))
    
    data = crypto_classifier(cryptogramm_header, cryptogramm_binary, cryptogramm_hexsym)
    if data[1] == "RSA":
        class_path, crypto_type, data, keys = data
        key, public_key_N, public_key_e = keys
        open(os.path.join(class_path, "RSA." + fname + ".txt"), "w").write(" ".join(keys))
        cryptogramm_binary = data
        output_fname = "e={}.{}".format(public_key_e, fname)
    else:
        output_fname = fname
        class_path, crypto_type = data
    # Ко всем бинарникам
    open(os.path.join(PATH_TO_BIN, output_fname), "wb").write(cryptogramm_binary)
    # Исходная криптограмма в класс
    shutil.copy(os.path.join(PATH_TO_FILES, fname), 
             os.path.join(class_path, output_fname))
    # Данные криптограммы в класс
    open(os.path.join(class_path, "BIN." + output_fname), "wb").write(cryptogramm_binary)
    #print(crypto_type, class_path, output_fname)