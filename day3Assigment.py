import os
import argparse
import datetime as dt

#Write a simple script to find a file  smaller X days old. X can be any number, let say 7 days.

my_parse = argparse.ArgumentParser(description='Reading thr directory path to find the file smaller than ')
my_parse.add_argument("pathname", help='Enter a directory path')
my_parse.add_argument("day", help='enter a number a day')
args = my_parse.parse_args()
dtnow = dt.datetime.now()
for dirpath, dirname, filename in os.walk(args.pathname):

    for file in filename:
        fullpath = os.path.join(dirpath, file)
        dtfile = dt.datetime.fromtimestamp(os.path.getmtime(fullpath))
        # print(dtfile)
        if (dtnow - dtfile).days < int(args.day):
            print(fullpath)


