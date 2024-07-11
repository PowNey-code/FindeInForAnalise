from sys import exit
import sets
import functions as fn

# получаем ключевые слова
tuple_key_words = fn.read_key_word()
if tuple_key_words is False:
    print('Ключевые слова не найдены')
    exit()

print('Ключевые слова:', tuple_key_words)


# Получаем список файлов
tuple_files = fn.get_tuple_files()
if tuple_files is False:
    print('Файлы в которых необходимо производить поиск отсутствуют.')
    exit()

print('Список файлов:', tuple_files)


# Получаем содержимое файлов
for file in tuple_files:
    print(fn.read_any_text_file(file))
