import unittest

class Test06(unittest.TestCase):

    def setUp(self):
        print("Test06 --> setUp被执行了")
    def tearDown(self):
        print("Test06 --> tearDown被执行了")
    def test06(self):
        print("test06被执行了")