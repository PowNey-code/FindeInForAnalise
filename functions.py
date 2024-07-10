from os.path import join, isfile
from os import walk
import sets

def read_key_word(file_name: str = 'list_of_KeyWords.txt') -> tuple | bool:
    if isfile(f'{sets.P}/{file_name}') is False:
        return False

    rows = ()
    with open(f'{sets.P}/{file_name}', encoding='utf-8') as file:
        for row in file.readlines():
            if '#' in row:
                continue
            rows += (row,)

    if len(rows) == 0:
        return False
    return rows


# Составляем список файлов
def get_tuple_files(folder: str = join(sets.P, sets.default_dir_with_files)) -> tuple[str, ...]:
    """ Search in pointed folder files which matched with pattern_name_files 

    Args:
        folder (str): Folder in which will be the search . Defaults folder ./files.
    """
    tuple_files_in_function: tuple[str, ...] = ()
    for(root, dirs, files) in walk(folder, True):
        for file in files:
            for pattern in sets.pattern_name_files:
                if pattern in file[-5:]:
                    tuple_files_in_function += (join(root, file),)
    return tuple_files_in_function
