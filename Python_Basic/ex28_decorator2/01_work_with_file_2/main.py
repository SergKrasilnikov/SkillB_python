from typing import TextIO, Optional

class File:
    """
    Контекст менеджер для работы с файлом

    Args:
        file (str): путь к файлу
        flag (str): режим работы с файлом

    Attributes:
        file (str): путь к файлу
        flag (str): режим работы с файлом
    """
    def __init__(self, file: str, flag: str) -> None:
        self.file = file
        self.flag = flag

    def __enter__(self) -> TextIO:
        """ При IOError открывается файл для записи """
        try:
            self.fp = open(self.file, self.flag)
        except IOError:
            self.fp = open(self.file, "w")
        return self.fp

    def __exit__(self, exp_type, exp_value, exp_tr) -> Optional[bool]:
        """ Подавляем все исключения IOError """
        if exp_type is IOError:
            self.fp.close()
            return True
        self.fp.close()

with File("asd.txt", "w") as fp:
    fp.write("Hello, World\n")

# COMMENT второй вариант
# class File:
#     def __init__(self, filename, mode):
#         self.filename = filename
#         self.mode = mode
#         self.file = None
#
#     def __enter__(self):
#         self.file = open(self.filename, self.mode)
#         return self.file
#
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         self.file.close()
#
# make_file = File('example.txt', 'r')
# try:
#     make_file.__enter__()
# except:
#     with open('example.txt', 'w') as file:
#         file.write('Test text.')