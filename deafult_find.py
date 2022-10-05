"""
finds all files containing a string in name 
"""
import argparse
from sys import exit as gentle_exit
import os
from re import search as research

def get_arguments():
    """
    takes the arguments
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("regular_expression", help="path to the first file", type=str)
    parser.add_argument("start_of_search", help="path to the first file", type=str)
    args = parser.parse_args()
    # path_to_start = r'{}'.format(args.start_of_search)
    if os.path.isdir(args.start_of_search):
        return args.regular_expression, args.start_of_search
    print('the second argument is incorrect')
    gentle_exit()

def operating_function(regular_expression, start_of_search):
    """
    searches through the files
    """
    res = []
    for directory in os.walk(start_of_search):
        for file_name in directory[2]:
            if research(regular_expression, file_name):
                res.append(os.path.normpath(os.path.join(\
                    directory[0], file_name)))
    if res == []:
        return "Nothing found"
    res = '\n'.join(res)
    return res

if __name__ == "__main__":
    arguments = get_arguments()
    print(operating_function(arguments[0], arguments[1]))
