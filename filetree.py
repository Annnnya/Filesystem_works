"""
prints files tree from current repository
"""
import argparse
from sys import exit as gentle_exit
import os

def main():
    """
    does pretty much everything
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("src", help="path to the directory", type=str)
    args = parser.parse_args()
    if not os.path.isdir(args.src):
        print("The directory doesn't exist")
        gentle_exit()
    print('./')
    recursive_form(args.src, 0)

def recursive_form(start, i):
    """
    doc
    """
    dirlst = os.listdir(start)
    for name in dirlst:
        if os.path.isfile(os.path.join(start, name)):
            print(" │  "*i, '├──' + name + '')
        if os.path.isdir(os.path.join(start, name)):
            print(" │  "*i,'├──' + name + '/')
            if os.listdir(os.path.join(start, name)) !=[]:
                i+=1
                recursive_form(os.path.join(start, name), i)
                i-=1

if __name__ == "__main__":
    main()
