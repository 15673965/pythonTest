import unittest

class Test07(unittest.TestCase):

    def setUp(self):
        print("Test07 --> setUp被执行了")
    def tearDown(self):
        print("Test07 --> tearDown被执行了")
    def test07(self):
        print("test07被执行了")