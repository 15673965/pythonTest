import unittest

class Test10(unittest.TestCase):

    def setUp(self):
        print("Test10 --> setUp被执行了")
    def tearDown(self):
        print("Test10 --> tearDown被执行了")
    def test10(self):
        print("test10被执行了")