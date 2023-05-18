import os
import time
import codecs

filename = "log.txt"
file_size = os.stat(filename).st_size

while True:
    current_size = os.stat(filename).st_size
    if current_size > file_size:
        with codecs.open(filename, 'r', encoding='utf-8') as f:
            f.seek(file_size)
            new_data = f.read()
            print(new_data, end='')
            file_size = current_size
    time.sleep(1)
