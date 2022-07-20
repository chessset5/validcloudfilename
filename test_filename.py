import unittest
import filename

class Test_stringClean(unittest.TestCase):
    def test_badstrings(self):
        self.assertEqual(filename.stringClean("f//alamf3fw0"),"f  alamf3fw0")

if __name__ == '__main__':
    unittest.main()
