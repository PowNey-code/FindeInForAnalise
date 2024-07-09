from sys import exit
from os.path import dirname, abspath, join, isfile
from os import walk


P = dirname(abspath(__file__))
file_with_key_words = 'list_of_KeyWords.txt'
dir_with_files = 'files'
pattern_name_files = ('.txt', '.doc', '.odt', '.rtf')

def read_key_word(file_name: str = 'list_of_KeyWords.txt') -> tuple | bool:
    if isfile(f'{P}/{file_name}') is False:
        return False

    rows = ()
    with open(f'{P}/{file_name}', encoding='utf-8') as file:
        for row in file.readlines():
            if '#' in row:
                continue
            rows += (row,)

    if len(rows) == 0:
        return False
    return rows

# получаем ключевые слова
tuple_key_words = read_key_word()
if tuple_key_words is False:
    print('Ключевые слова не найдены')
    exit()

print('Ключевые слова:', tuple_key_words)

# Составляем список файлов
tuple_files = ()
for(root, dirs, files) in walk(join(P, dir_with_files), True):
    for file in files:
        for pattern in pattern_name_files:
            if pattern in file[-5:]:
                tuple_files += (join(root, file),)

print('Список файлов:', tuple_files)


