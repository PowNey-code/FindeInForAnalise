from os.path import dirname, abspath

P: str = dirname(abspath(__file__))
file_with_key_words = 'list_of_KeyWords.txt'
user_dir_with_files = 'files'
default_dir_with_files = 'files'
pattern_name_files: tuple[str, ...] = ('.txt', '.doc', '.odt', '.rtf')