'''
This file is a script that runs through and renames files in the current and all sub directories.
'''

import os
import _osx_support as osx

# https://www.adamsmith.haus/python/answers/how-to-traverse-a-directory-in-python
# https://docs.python.org/3/library/platform.html


def main():
    thisandlowerrename()
    # printdirtf()
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
        # Gets the file name of a string if there is one
        ret = ""
        dotpos = input.rfind(".")
        if dotpos > 0:
            # ret = dotpos to end of str
            ret = input[dotpos:]
            if(not ret[1:].isalnum()):
                ret = ""
        return ret

    def incFileName(self, input) -> str:
        # Increment File Name if input can be recognised
        if type(input) == str:
            return self.incFileNameS(input)
        if type(input) == tuple:
            return self.incFileNameT(input)
        if type(input) == list:
            if len(input) == 2:
                return self.incFileNameT(tuple(input))
        return str(input)

    def incFileNameS(self, input: str) -> str:
        # Increment File Name, String Input
        filename, filetype = (self.fileSplit(input))
        return self.__incFileName(filename, filetype)

    def incFileNameHT(self, filename: str, filetype: str) -> str:
        # Increment File Name, Head String, Tail String Input
        return self.__incFileName(filename, filetype)

    def incFileNameT(self, input: tuple[str, str]) -> str:
        # Increment File Name, String Input
        return self.__incFileName(input[0], input[1])

    def __incFileName(self, filename: str, filetype: str) -> str:
        # Increment File Name, String Input

        # "inline" function for a file with no increment, ie (#), yet.
        def __newIncFile(oldname: str) -> str:
            return oldname + "(0)"

        if(filename[-1] != ")"):
            filename = __newIncFile(filename)
        else:  # filename[-1] == ")"
            # eg: apple(1).txt -> 1
            num = filename[filename.rfind("(")+1:filename.rfind(")")]
            sign = 1

            # negative number value
            if(num[0] == "-"):
                # str().isdigit() will return False if the number is negative, ie "-1".isdigit() == False
                # so we have to do this stupid thing
                sign = (-1)
                num = num[1:]  # apple -> pple

            # new file name
            nfn = filename[:filename.rfind("(")]
            if (num.isdigit() == False):
                filename = __newIncFile(filename)
            else:  # num.isdigit() == True
                num = sign*int(num)
                num = int(num) + 1
                filename = nfn + "(" + str(num) + ")"

        return filename + filetype

    def fileSplit(self, input: str) -> tuple[str, str]:
        # returns file name and file type respectfully
        tail = self.getFileType(input)
        head = input.removesuffix(tail)
        return [head, tail]


def thisandlowerrename():
    # Traverses the directories from the script
    # to the end of the subdirectories scanning
    # and fixing invalid names

    # path is a list of "tuple" [{str,list,list}], currnet dir path, list of child dir names, list of file name
    path = os.walk(".")
    ignorelist = [str()]
    ignorelist.append(".DS_Store")

    for dirpath, dirnames, filenames in path:
        s = filestring()  # for filestring() functions

        # find files to rename
        for i in range(len(filenames)):
            # if in ignore list go to next item
            if filenames[i] in ignorelist:
                continue

            # new file name
            nfn = s.removeDiplicateSpaces(s.stringClean(filenames[i]))

            # if no new name change, go to next file.
            if nfn == filenames[i]:
                continue

            # check if new file name isn't already used in dir
            while(nfn in filenames):
                nfn = s.incFileNameS(nfn)

            # rename the file
            os.renames(os.path.join(
                dirpath, filenames[i]), os.path.join(dirpath, nfn))

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
