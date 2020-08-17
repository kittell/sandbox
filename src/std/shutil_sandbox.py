import os
from os import path
import shutil
from shutil import make_archive
from zipfile import ZipFile

filename = 'testfile.txt'
if path.exists(filename):
    src = path.realpath(filename)
    dst = src + '.bak'
#     shutil.copy(src, dst)
#     shutil.copystat(src, dst)

#     root_dir, tail = path.split(src)
#     shutil.make_archive('archive', 'zip', root_dir)

    with ZipFile('testzip.zip', 'w') as newzip:
        newzip.write(filename)
        newzip.write(filename + '.bak')