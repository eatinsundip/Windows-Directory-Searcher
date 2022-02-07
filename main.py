from os import system as cmd
from os import listdir as ls

'''
I know this is just a fancy grep tool but it worked for what I needed it for and I may use it again someday?
'''

SearchString = '' # Set This
dir = '' # Directory in which you're searching for a keyword

for file in ls(dir):
    if '.txt' in file:
        file_path = f'{dir}\'{file}\''
        print(file_path)
        cmd(f'type {file_path} | findstr {SearchString}')