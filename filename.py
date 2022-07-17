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


# '
import os
import _osx_support as osx


def main():
    path = os.walk(".")
    for root, directories, files in path:
        for directory in directories:
            print(directory)
        for file in files:
            print(file)
    return


# Takes in a string and removes all invalid characters accoring to OneNote
def stringClean(input: str) -> str:
    badString = "\"/\*:?|<>"
    output = ""
    for c in input:
        if c in badString:
            output += " "
        else:
            output += c
    return output


def findNextString():
    return


if __name__ == "__main__":
    main()