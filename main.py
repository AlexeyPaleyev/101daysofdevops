

import os
import pathlib

try:
    with open("abc.txt") as f:
        a = f.read()
except Exception as e:
    print(e)


fl = "c:\windows\system32\drivers\etc\hosts"
if os.path.exists(fl) and os.path.isfile(fl):
    print("file ", fl, " ", "exist")
else:
    print("file ", fl, " ", "not exist")

path = pathlib.Path(fl)
print(path.exists())
print(path.is_file())
print(path.is_dir())



