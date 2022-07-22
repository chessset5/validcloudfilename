# https://code.visualstudio.com/docs/python/testing
# from .. import filename
import filename
import unittest


class Test_stringCleanBadString(unittest.TestCase):
    # bad strings
    s = filename.stringclean()

    def test_badstrings0(self):
        self.assertEqual(self.s.stringClean("f//alamf3fw0"), "f  alamf3fw0")

    def test_badstrings1(self):
        self.assertEqual(self.s.stringClean("CS 131/CSCI 1310/ Fundamentals of Computer Systems"),
                         "CS 131 CSCI 1310  Fundamentals of Computer Systems")


class Test_stringCleanWorseString(unittest.TestCase):
    # worse string
    s = filename.stringclean()

    def test_worsestrings0(self):
        self.assertEqual(self.s.stringClean("\u200B\u200B\u200B"), "   ")

    def test_worsestrings1(self):
        self.assertEqual(self.s.stringClean(
            "\u200B\u200B\u200B\u0020"), "    ")

    def test_worsestrings2(self):
        self.assertEqual(self.s.stringClean("\u0020\u00A0\u1680\u180E\u2000\u2001\
\u2002\u2003\u2004\u2005\u2006\u2007\
\u2008\u2009\u200A\u200B\u202F\u205F\
\u3000\uFEFF"), "                   ")

    def test_worsestrings3(self):
        self.assertEqual(self.s.stringClean("a\u0020\u00A0\u1680\u180Ea\u2000\u2001\
\u2002\u2003\u2004\u2005\u2006\u2007\
\u2008a\u2009\u200A\u200B\u202F\u205F\
\u3000\uFEFF"), "a    a         a       ")


class Test_removeDiplicateSpaces(unittest.TestCase):
    s = filename.stringclean()

    def test_removeDiplicateSpaces0(self):
        self.assertEqual(self.s.removeDiplicateSpaces("a    a"), "a a")

    def test_removeDiplicateSpaces1(self):
        self.assertEqual(self.s.removeDiplicateSpaces("   a     "), " a ")

    def test_removeDiplicateSpaces2(self):
        self.assertEqual(self.s.removeDiplicateSpaces("a    a   a"), "a a a")

    def test_removeDiplicateSpaces3(self):
        self.assertEqual(self.s.removeDiplicateSpaces(""), "")

    def test_removeDiplicateSpaces4(self):
        self.assertEqual(self.s.removeDiplicateSpaces("        "), " ")

    def test_removeDiplicateSpaces5(self):
        self.assertEqual(self.s.removeDiplicateSpaces("  "), " ")

    def test_removeDiplicateSpaces6(self):
        self.assertEqual(self.s.removeDiplicateSpaces(" "), " ")


if __name__ == '__main__':
    unittest.main()
