import os
import argparse

fl = "c:\!Alx\luxoft"
# print(list(os.walk(fl)))
my_parse = argparse.ArgumentParser(description='Reading thr directory path to find the file')
my_parse.add_argument("pathname", help='Enter a directory path')
my_parse.add_argument("filename", help='enter a file name')
args = my_parse.parse_args()

for dirpath, dirname, filename in os.walk(fl):

    for file in filename:

        if file == args.filename:
            print(os.path.join(dirpath, file))

