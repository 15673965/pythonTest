import unittest

class Test09(unittest.TestCase):

    def setUp(self):
        print("Test09 --> setUp被执行了")
    def tearDown(self):
        print("Test09 --> tearDown被执行了")
    def test09(self):
        print("test09被执行了")