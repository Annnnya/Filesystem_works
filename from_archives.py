"""
creates one file from data in different archives
"""
import argparse
from sys import exit as gentle_exit
import os
import zipfile

def get_arguments():
    """
    takes the arguments;
    creates a common file for every archive
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("src1", help="path to the first file", type=str)
    parser.add_argument("src2", help="path to the second file", type=str)
    parser.add_argument("dst", help="path to the otput file", type=str)
    args = parser.parse_args()
    if os.path.exists(args.dst):
        print("The output file already exists")
        gentle_exit()
    elif not os.path.exists(args.src1):
        print("The first path is incorrect")
        gentle_exit()
    elif not os.path.exists(args.src2):
        print("The second path is incorrect")
        gentle_exit()
    return read_set(args.src1, 'src1_file'), read_set(args.src2, 'src2_file'), args.dst

def read_set(src_path, extr_name):
    """
    reads through the archive ans creates set of lines
    """
    res = set()
    try:
        with zipfile.ZipFile(src_path, 'r') as zip1:
            zip1.extractall(extr_name)
            for directory in os.walk(extr_name):
                for file_name in directory[2]:
                    with open(os.path.normpath(os.path.join(\
                        directory[0], file_name)), 'r', encoding='utf-8') as file:
                        for line in file:
                            res.add(line.strip('\n'))
                    os.remove(os.path.normpath(os.path.join(\
                        directory[0], file_name)))
                try:
                    os.removedirs(directory[0])
                except OSError:
                    continue
        return res
    except zipfile.BadZipFile:
        print("Something's wrong with your zip file :-(")
        gentle_exit()

def result(sets):
    """
    does the thing
    """
    res = '\n'.join(sorted(list(sets[0]&sets[1])))
    with open(sets[2], 'w', encoding='utf-8') as file:
        file.write(res)

if __name__ == "__main__":
    result(get_arguments())
