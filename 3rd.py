# WAPP to check the file size

import os

file_stat = os.stat('my_file.txt')
print(file_stat.st_size)