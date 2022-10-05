"""
creates archive from files with regex in name
"""
import argparse
from sys import exit as gentle_exit
import os
import zipfile
from re import search as research

def get_arguments():
    """
    takes the arguments
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("regular_expression", help="expression to search", type=str)
    parser.add_argument("path_to_archive", help="path to the archive", type=str)
    parser.add_argument("path_to_result", help="path to the result", type=str)
    args = parser.parse_args()
    if not os.path.exists(args.path_to_archive):
        print("The path to archive is incorrect")
        gentle_exit()
    if not os.path.exists(args.path_to_result):
        print("The path to resulting archive is incorrect")
        gentle_exit()
    return args.regular_expression, args.path_to_archive, args.path_to_result

def searcher(inputs):
    """
    finds the files and wrires them into the archive
    """
    try:
        with zipfile.ZipFile(inputs[1], 'r') as arch:
            with zipfile.ZipFile(inputs[2], 'w') as res_zip:
                arch.extractall('extr')
                for directory in os.walk('extr'):
                    for file_name in directory[2]:
                        file_name_path = os.path.normpath(os.path.join(directory[0], file_name))
                        if research(inputs[0], file_name):
                            temp_file =os.path.normpath(os.path.join(os.getcwd(), file_name))
                            os.rename(file_name_path, temp_file)
                            res_zip.write(file_name)
                            os.remove(temp_file)
                        else:
                            os.remove(file_name_path)
                    try:
                        os.removedirs(directory[0])
                    except OSError:
                        continue
    except zipfile.BadZipFile:
        print("Something's wrong with your zip file :-(")
        gentle_exit()

if __name__=="__main__":
    myargs = get_arguments()
    searcher(myargs)
