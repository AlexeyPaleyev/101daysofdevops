import os
import argparse
import datetime as dt
import pathlib

#Write a simple script to find a file  smaller X days old. X can be any number, let say 7 days.

my_parse = argparse.ArgumentParser(description='Reading thr directory path to find the file smaller than ')
my_parse.add_argument("pathname", help='Enter a directory path')
my_parse.add_argument("day", help='enter a number a day')
my_parse.add_argument("fltype", help='enter file ext', nargs='?', type=str, const='')

args = my_parse.parse_args()
dtnow = dt.datetime.now()

def isyangest(dtnow, dtfile, day):
    return (dtnow - dtfile).days < day


for dirpath, dirname, filename in os.walk(args.pathname):

    for file in filename:
        fullpath = os.path.join(dirpath, file)
        dtfile = dt.datetime.fromtimestamp(os.path.getmtime(fullpath))
        # print(dtfile)

        fl = ((args.fltype == None) or (pathlib.Path(fullpath).suffix[1:] == args.fltype))
        #print(args.fltype == '', pathlib.Path(fullpath).suffix, args.fltype)
        #print(args.fltype == None, pathlib.Path(fullpath).suffix == args.fltype, pathlib.Path(fullpath).suffix[1:], args.fltype)
        if (isyangest(dtnow, dtfile, int(args.day)) and fl):
            print(fullpath)


