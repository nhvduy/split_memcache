import unittest
from mylibs.big_file import MyLib
import os
lib = MyLib()
class TestLib(unittest.TestCase):
    def test_notexist(self):
        name = "abc"
        result = lib.get_file(name)
        self.assertEqual(result, "File doest not exists.")

    def test_exist(self):
        name = "file2"
        file_path = os.path.abspath("./file2.dat")
        f = open(file_path, "rb")
        result = lib.set_file(name, f)
        self.assertEqual(result, "File already exists.")
        f.close()

if __name__ == '__main__':
    unittest.main()