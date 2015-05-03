__author__ = 'yinyan, shichanghui'

from PGM import *
from PPM import *
from sys import stdin
from sys import argv


def main():
    if len(argv) > 5:
        if argv[1] == "P2":
            pic = PGM()
        elif argv[1] == "P3":
            pic = PPM()
    else:
        pic = PGM()
    pic.save_file()
main()