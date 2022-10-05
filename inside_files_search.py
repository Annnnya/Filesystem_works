"""
Searches regex1 in file names starting from current directory
Inside all found files searches regex2
"""
import argparse
from sys import exit as gentle_exit
import os
from re import search as research

def main():
    """
    takes the arguments and outputs everything
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("expr", help="substring that needs to be found and replaced", type=str)
    parser.add_argument("filesubstr", help="expression for files to search", type=str)
    parser.add_argument("--show_lines", help="change the file or output in console",\
         action="store_true")
    parser.add_argument("--only_show_counts", help="change the file or output in console",\
         action="store_true")
    args = parser.parse_args()
    if args.only_show_counts and args.show_lines:
        print("Choose one optional argument")
        gentle_exit()
    if args.show_lines:
        searching_func2(args.expr, args.filesubstr)
    elif args.only_show_counts:
        searching_func3(args.expr, args.filesubstr)
    else:
        searching_func1(args.expr, args.filesubstr)

def searching_func2(substr, subnm):
    """
    searches with show_lines
    """
    for directory in os.walk(os.getcwd()):
        for file_name in directory[2]:
            if research(subnm, file_name):
                with open(os.path.normpath(os.path.join(\
                    directory[0], file_name)), 'r', encoding='utf-8') as file:
                    counts=1
                    fnd = False
                    for line in file:
                        if research(substr, line):
                            if not fnd:
                                print('\n', file_name, sep='')
                                fnd = True
                            print(counts, ":", line.strip('\n'))
                        counts+=1

def searching_func1(substr, subnm):
    """
    searches without optional arguments
    """
    for directory in os.walk(os.getcwd()):
        for file_name in directory[2]:
            if research(subnm, file_name):
                with open(os.path.normpath(os.path.join(\
                    directory[0], file_name)), 'r', encoding='utf-8') as file:
                    fnd = False
                    for line in file:
                        if research(substr, line):
                            if not fnd:
                                print('\n', file_name, sep='')
                                fnd = True
                            print(line.strip('\n'))

def searching_func3(substr, subnm):
    """
    searches with only_show_counts
    """
    for directory in os.walk(os.getcwd()):
        for file_name in directory[2]:
            if research(subnm, file_name):
                with open(os.path.normpath(os.path.join(\
                    directory[0], file_name)), 'r', encoding='utf-8') as file:
                    counts=0
                    fnd = False
                    for line in file:
                        if research(substr, line):
                            fnd = True
                            counts+=1
                    if fnd:
                        print('\n', file_name, sep='') 
                        print(counts)

if __name__=="__main__":
    main()
