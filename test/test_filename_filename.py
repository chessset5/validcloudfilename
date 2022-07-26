import filename
import unittest


class Test_returnFileType(unittest.TestCase):
    s = filename.filestring()

    def test_getFileType1(self):
        self.assertEqual(self.s.getFileType(".DS_Store"), "")

    def test_getFileType2(self):
        self.assertEqual(self.s.getFileType("__pycache__"), "")

    def test_getFileType3(self):
        self.assertEqual(self.s.getFileType("apple.txt"), ".txt")

    def test_getFileType4(self):
        self.assertEqual(self.s.getFileType("apple.(021)txt"), "")


class Test_fileSplit(unittest.TestCase):
    s = filename.filestring()

    def test_filesplit0(self):
        self.assertEqual(self.s.fileSplit("apple.txt"), ["apple", ".txt"])

    def test_filesplit1(self):
        self.assertEqual(self.s.fileSplit("appletxt"), ["appletxt", ""])

    def test_filesplit2(self):
        self.assertEqual(self.s.fileSplit(".appletxt"), [".appletxt", ""])

    def test_filesplit3(self):
        self.assertEqual(self.s.fileSplit("appletxt"), ["appletxt", ""])

    def test_filesplit4(self):
        self.assertEqual(self.s.fileSplit("apple.test(1213)"),
                         ["apple.test(1213)", ""])


class Test_oneIncFileName(unittest.TestCase):
    s = filename.filestring()

    def test_1ifn0(self):
        self.assertEqual(self.s.incFileName("apple.txt"), "apple(0).txt")

    def test_1ifn1(self):
        self.assertEqual(self.s.incFileName("apple(-5).txt"), "apple(0).txt")

    def test_1ifn2(self):
        self.assertEqual(self.s.incFileName("apple(-1).txt"), "apple(0).txt")

    def test_1ifn3(self):
        self.assertEqual(self.s.incFileName("apple(0).txt"), "apple(1).txt")

    def test_1ifn3(self):
        self.assertEqual(self.s.incFileName(
            "apple(3456).txt"), "apple(3457).txt")

    def test_1ifn4(self):
        self.assertEqual(self.s.incFileName("apple(-1)).txt"),
                         "apple(-1))(0).txt")

    def test_1ifn5(self):
        self.assertEqual(self.s.incFileName("(0)apple.txt"), "(0)apple(0).txt")

    def test_1ifn6(self):
        self.assertEqual(self.s.incFileName("(apple).txt"), "(apple)(0).txt")

    def test_1ifn0_1(self):
        self.assertEqual(self.s.incFileName("apple"), "apple(0)")

    def test_1ifn1_1(self):
        self.assertEqual(self.s.incFileName("apple(-5)."), "apple(-5).(0)")

    def test_1ifn2_1(self):
        self.assertEqual(self.s.incFileName("apple(-1)"), "apple(0)")

    def test_1ifn3_1(self):
        self.assertEqual(self.s.incFileName("apple(0)"), "apple(1)")

    def test_1ifn3_1(self):
        self.assertEqual(self.s.incFileName(
            ".apple(3456)"), ".apple(3457)")

    def test_1ifn3_1_1(self):
        self.assertEqual(self.s.incFileName(
            ".app.le(3456)"), ".app.le(3457)")

    def test_1ifn4_1(self):
        self.assertEqual(self.s.incFileName("apple(-1)).txt"),
                         "apple(-1))(0).txt")

    def test_1ifn5_1(self):
        self.assertEqual(self.s.incFileName("(0)apple.txt"), "(0)apple(0).txt")

    def test_1ifn6_1(self):
        self.assertEqual(self.s.incFileName("(apple).txt"), "(apple)(0).txt")

    def test_1ifn7(self):
        self.assertEqual(self.s.incFileName(
            "(apple)(0).txt(0)"), "(apple)(0).txt(1)")


class Test_tupleIncFileName(unittest.TestCase):

    s = filename.filestring()

    def test_1ifn0(self):
        self.assertEqual(self.s.incFileName(["apple", ".txt"]), "apple(0).txt")

    def test_1ifn1(self):
        self.assertEqual(self.s.incFileName([
            "apple(-5)", ".txt"]), "apple(0).txt")

    def test_1ifn2(self):
        self.assertEqual(self.s.incFileName([
            "apple(-1)", ".txt"]), "apple(0).txt")

    def test_1ifn3(self):
        self.assertEqual(self.s.incFileName([
            "apple(0)", ".txt"]), "apple(1).txt")

    def test_1ifn3(self):
        self.assertEqual(self.s.incFileName([
            "apple(3456)", ".txt"]), "apple(3457).txt")

    def test_1ifn4(self):
        self.assertEqual(self.s.incFileName(["apple(-1))", ".txt"]),
                         "apple(-1))(0).txt")

    def test_1ifn5(self):
        self.assertEqual(self.s.incFileName([
            "(0)apple", ".txt"]), "(0)apple(0).txt")

    def test_1ifn6(self):
        self.assertEqual(self.s.incFileName([
            "(apple)", ".txt"]), "(apple)(0).txt")


class Test_tupleIncFileNameT(unittest.TestCase):

    s = filename.filestring()

    def test_1ifn0(self):
        self.assertEqual(self.s.incFileNameT(
            ["apple", ".txt"]), "apple(0).txt")

    def test_1ifn1(self):
        self.assertEqual(self.s.incFileNameT([
            "apple(-5)", ".txt"]), "apple(0).txt")

    def test_1ifn2(self):
        self.assertEqual(self.s.incFileNameT([
            "apple(-1)", ".txt"]), "apple(0).txt")

    def test_1ifn3(self):
        self.assertEqual(self.s.incFileNameT([
            "apple(0)", ".txt"]), "apple(1).txt")

    def test_1ifn3(self):
        self.assertEqual(self.s.incFileNameT([
            "apple(3456)", ".txt"]), "apple(3457).txt")

    def test_1ifn4(self):
        self.assertEqual(self.s.incFileNameT(["apple(-1))", ".txt"]),
                         "apple(-1))(0).txt")

    def test_1ifn5(self):
        self.assertEqual(self.s.incFileNameT([
            "(0)apple", ".txt"]), "(0)apple(0).txt")

    def test_1ifn6(self):
        self.assertEqual(self.s.incFileNameT([
            "(apple)", ".txt"]), "(apple)(0).txt")
