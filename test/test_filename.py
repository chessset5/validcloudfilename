# https://code.visualstudio.com/docs/python/testing
# from .. import filename
import filename
import unittest


class Test_stringClean(unittest.TestCase):
    def test_badstrings(self):

        # bad strings
        self.assertEqual(filename.stringClean("f//alamf3fw0"), "f  alamf3fw0")

        # worse string
        self.assertEqual(filename.stringClean("\u200B\u200B\u200B"), "")
        self.assertEqual(filename.stringClean("\u200B\u200B\u200B"), "")
        self.assertEqual(filename.stringClean("\u0020\u00A0\u1680\u180E\u2000\u2001\
            \u2002\u2003\u2004\u2005\u2006\u2007\
            \u2008\u2009\u200A\u200B\u202F\u205F\
            \u3000\uFEFF"), "")

    def test_removeDiplicateSpaces(self):
        self.assertEqual(filename.removeDiplicateSpaces("a    a"), "a a")
        self.assertEqual(filename.removeDiplicateSpaces("   a     "), " a ")
        self.assertEqual(filename.removeDiplicateSpaces("a    a   a"), "a a a")
        self.assertEqual(filename.removeDiplicateSpaces(""), "")
        self.assertEqual(filename.removeDiplicateSpaces("        "), " ")


if __name__ == '__main__':
    unittest.main()
