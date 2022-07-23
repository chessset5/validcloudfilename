'''
# This file is a script that runs through and renames files in the current and all sub directories.
'''

import os
import _osx_support as osx
from turtle import dot


'''
TODO:
  Scan through ever file and directory of the OneDrive.
  Check each file and folders name
  Make sure each file and folder has a legal name
      Make sure that all the characters in the file or folder does not contain an illegal character
          If the name is illegal, clean it
              If there is an illegal character replace it with a space
'''

# https://www.adamsmith.haus/python/answers/how-to-traverse-a-directory-in-python
# https://docs.python.org/3/library/platform.html


def main():
    # thisandlowerrename()
    printdirtf()
    return


class filestring:
    # string cleaning class

    # Characters invalid for OneDrive.
    __badString = "\"/\*:?|<>"
    # Unicode white space characters that could cause problems.
    __worseString = "\u0020\u00A0\u1680\u180E\u2000\u2001\
                    \u2002\u2003\u2004\u2005\u2006\u2007\
                    \u2008\u2009\u200A\u200B\u202F\u205F\
                    \u3000\uFEFF"
    # Superseeds bad and worse strings.
    __goodString = ""

    def __init__(self):
        # removing good space in worseString
        self.__worseString = self.__worseString.replace(" ", "")

    def addToGoodString(self, input: str) -> str:
        self.__goodString += input
        return self.__goodString

    def replaceGoodString(self, input: str) -> str:
        self.__goodString = input
        return self.__goodString

    def addToBadString(self, input: str) -> str:
        self.__badString += input
        return self.__badString

    def replaceBadString(self, input: str) -> str:
        self.__badString = input
        return self.__badString

    def addToWorseString(self, input: str) -> str:
        self.__worseString += input
        return self.__worseString

    def removeDiplicateSpaces(self, input: str) -> str:
        # eg "a    a" -> "a a", "a   a  b" -> "a a b"
        ret = str()
        for c in input:
            ret += c
            if ret.__len__() > 1:
                if (c == ' ') and (ret[-2] == c):
                    ret = ret[:-1]
        return ret

    def containsBadChar(self, input: str) -> bool:
        # contains true if bad string
        output = ""
        for c in input:
            if c in self.__goodString:
                continue
            elif (c in self.__badString) or (c in self.__worseString):
                return True
        return False

    def stringClean(self, input: str) -> str:
        # Takes in a string and removes all invalid characters accoring to OneDrive
        output = ""
        for c in input:
            if c in self.__goodString:
                output += c
            elif (c in self.__badString) or (c in self.__worseString):
                output += " "
            else:
                output += c
        return output

    def getFileType(self, input: str) -> str:
        ret = ""
        dotpos = input.rfind(".")
        if dotpos > 0:
            # ret = dotpos to end of str
            ret = input[dotpos:]
        return ret


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
    ignorelist = [str()]
    ignorelist.append(".DS_Store")

    for dirpath, dirnames, filenames in path:
        s = filestring()
        renamepos = [False]*(len(filenames))
        renamelst = filenames

        # find files to rename
        for i in range(len(filenames)):
            if filenames[i] in ignorelist:
                continue
            # new file name
            nfn = s.removeDiplicateSpaces(s.stringClean(filenames[i]))

            # adding (#)
            c = 0
            while(nfn in renamelst):
                # -1 if there is no dot, like a pure data or make file
                dotpos = nfn.rfind(".")
                # not a .DS_Store Files
                if(dotpos != 0):
                    continue
            if (renamelst[i] != filenames[i]):
                renamepos[i] = True

        # renaming files
        for i in range(len(renamepos)):
            if renamepos[i] == True:
                # TODO: Figure out how rename and renames work
                os.rename(dirpath, dirpath)

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


if __name__ == "__main__":
    main()
