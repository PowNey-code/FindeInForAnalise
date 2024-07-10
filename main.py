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

# print('Список файлов:', tuple_files)


tuple_files = ('files/123.docx',)
for file in tuple_files:
    match file[-4:]:
        case 'docx':
            print('docx', fn.read_docx(file))

        # case '.doc':
        #     print('doc', fn.read_doc(file))

        case '.rtf':
            print('rtf', fn.read_rtf(file))

        case '.odt':
            print('odt', fn.read_odt(file))

        case '.txt':
            print('txt', fn.read_txt(file))

        case _:
            print('_', file)
