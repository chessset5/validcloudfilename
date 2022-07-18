r'''
# TODO:
#   Scan through ever file and directory of the OneDrive.
#   Check each file and folders name
#   Make sure each file and folder has a legal name
#       Make sure that all the characters in the file or folder does not contain an illegal character
#           If the name is illegal, clean it
#               If there is an illegal character replace it with a space
'''

# https://www.adamsmith.haus/python/answers/how-to-traverse-a-directory-in-python
# https://docs.python.org/3/library/platform.html

from msilib import _directories
import os
import _osx_support as osx


def main():
    # thisandlowerrename()
    printdirtf()
    return


def thisandlowerrename():
    # Traverses the directories from the script
    # to the end of the subdirectories scanning
    # and fixing invalid names
    '''
        TODO:
            Loop though the directories
                For each dir load all the file names into a set
                Make a list for renames
                loop Check all names against a character checker function
                    TODO:
                        Make Character Checker Function
                    If the name is bad run it through the stringClean() funciton
                    Add the name to the filename set
                    If the set size doesn't increase see if the file name has a postfix (#)
                    TODO:
                        Make a function that checks for postfix
                        Make a function that adds a postfix
                    loop until set size increases
                        If it does have a postfix, incriment current file
                        end loop
                end loop
            end loop
    '''

    # Testing VS Code using iPad OS Web App using GitHub

    path = os.walk(".")
    for dirpath, dirnames, filenames in path:

        break

    return


def printdirtf():
    # print directory to file
    #   This function takes the current directory and outputs
    path = os.walk(".", False)
    for root, directories, files in path:
        print("root:\t"+root)
        for directory in directories:
            print("\tdir:\td:"+directory)
        for file in files:
            print("\tfile:\tf:"+file)

    return


def stringClean(input: str) -> str:
    # Takes in a string and removes all invalid characters accoring to OneDrive
    badString = "\"/\*:?|<>"
    output = ""
    for c in input:
        if c in badString:
            output += " "
        else:
            output += c
    return output


if __name__ == "__main__":
    main()
