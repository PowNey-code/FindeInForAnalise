from typing import Literal
from os.path import join, isfile, isdir
from os import walk
import docx
from striprtf.striprtf import rtf_to_text
from odf import text, teletype
from odf.opendocument import load as odf_load
import sets

def read_key_word(file_name: str = 'list_of_KeyWords.txt') -> tuple[str, ...] | Literal[False]:
    """ Read file with key words. Format file should be '*.txt', each key word wried on new line.
        If new line start with symbol '##', that line skipped
    """
    if isfile(f'{sets.P}/{file_name}') is False:
        return False

    rows: tuple[str, ...] = ()
    with open(f'{sets.P}/{file_name}', encoding='utf-8') as file:
        for row in file.readlines():
            if '##' in row:
                continue
            rows += (row.strip(),)

    if len(rows) == 0:
        return False
    return rows

def get_tuple_files(folder: str = join(sets.P, sets.default_dir_with_files)) -> tuple[str, ...] | Literal[False]:
    """ Search in pointed folder files which matched with pattern_name_files 

        Args:
            folder (str): Folder in which will be the search . Defaults folder ./files.
    """
    if not isdir(folder):
        return False

    tuple_files_in_function: tuple[str, ...] = ()
    for(root, dirs, files) in walk(folder, True):
        for file in files:
            for pattern in sets.pattern_name_files:
                if pattern in file[-5:]:
                    tuple_files_in_function += (join(root, file),)

    if len(tuple_files_in_function) == 0:
        return False

    return tuple_files_in_function

def read_docx(file: str) -> tuple[str, ...] | Literal[False]:
    doc = docx.Document(file)
    paragraphs = doc.paragraphs
    if len(paragraphs) < 1:
        return False

    rows = *(paragraph.text for paragraph in paragraphs if paragraph.text != ''),
    return rows

def read_txt(file: str) -> tuple[str, ...] | Literal[False]:
    with open(file, encoding='utf-8') as f:
        rows = *(row.strip() for row in f.readlines()),

    if len(rows) == 0:
        return False
    return rows

def read_rtf(file: str) -> tuple[str, ...] | Literal[False]:
    with open(file=file, mode='r') as f:
        file_content=f.read()
    text_content=rtf_to_text(file_content)
    rows = text_content.split('\n')
    rows = *(row for row in rows if row != ''),

    if len(rows) == 0:
        return False

    return rows

def read_odt(file: str) -> tuple[str, ...] | Literal[False]:
    textdoc = odf_load(file)
    paragraphs = textdoc.getElementsByType(text.P)

    rows: tuple[str, ...] = ()
    for paragraph in paragraphs:
        row = teletype.extractText(paragraph)
        if row != '':
            rows += (row,)

    if len(rows) == 0:
        return False
    
    return rows